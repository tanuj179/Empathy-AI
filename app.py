from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import sqlite3
import openai
import os
from dotenv import load_dotenv

# Load OpenAI API Key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize Flask App
app = Flask(__name__)
app.secret_key = "super_secret_key"

# Flask-Login Setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# SQLite Database Connection
def create_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    conn.commit()
    conn.close()

create_db()

# User Model
class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# Home Route (Redirect to Register Page)
@app.route("/")
def home():
    return redirect(url_for("register"))


# Home (Redirect to Login)
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        # Check if username already exists
        cursor.execute("SELECT id FROM users WHERE username=?", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            conn.close()
            return render_template("register.html", error="❌ Username already exists. Please choose another.")

        # Insert new user
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()

        return redirect(url_for("login"))

    return render_template("register.html")

# Login Route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            login_user(User(user[0]))
            return redirect(url_for("chatbot"))

    return render_template("login.html")

# Logout Route
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

# Chatbot Route
@app.route("/chatbot")
@login_required
def chatbot():
    return render_template("chatbot.html")

# OpenAI Chatbot API Route
@app.route("/ask", methods=["POST"])
@login_required
def ask():
    user_input = request.json.get("message", "").strip()

    if not user_input:
        return jsonify({"response": "❌ Please enter a message."})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a mental health assistant providing calm and supportive responses."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7
        )

        reply = response["choices"][0]["message"]["content"].strip()
        return jsonify({"response": reply})

    except openai.error.AuthenticationError:
        return jsonify({"response": "❌ Invalid API Key. Please check your OpenAI API key."})
    except openai.error.RateLimitError:
        return jsonify({"response": "❌ Rate limit exceeded. Please wait before trying again."})
    except Exception as e:
        print("API Error:", str(e))
        return jsonify({"response": "❌ There was an error processing your request. Please try again later."})
# Run Flask App
if __name__ == "__main__":
    app.run(debug=True)
