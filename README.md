

# Empathy AI

🧠 Empathy AI is a mental health chatbot that provides emotional support using OpenAI's GPT-4o-mini.  
Built with Flask, SQLite, and OpenAI API, it helps users express their emotions in a safe and empathetic space.  

Features:  
✅ Secure Login & Registration with Flask-Login  
✅ AI-powered chatbot for mental health assistance  
✅ Responsive UI with psychological color scheme  
✅ SQLite database for user authentication  
✅ `.env` file support for API key security  
✅ Error handling for API rate limits & authentication issues  


## Installation
🔹 Step 1: Clone the Repository

```bash
git clone https://github.com/tanuj179/Empathy-AI.git

cd empathy-ai
```

## 🔹 Step 2: Set Up Virtual Environment

```python
python -m venv venv
```

## 🔹 Step 3: Activate Virtual Environment For windows

```python
venv\Scripts\activate
```


## 🔹 Step 4: Install Dependencies 

```python
pip install --upgrade pip 

pip install -r requirements.txt
```

## 🔹 Step 5: Create `.env` File for API Key 

```python
OPENAI_API_KEY= 'your_openai_api_key_here'
```

## 🔹  Step 6: Run Flask Application  
```python
python main.py
```

✅ **By default, the app will redirect to the Register Page (`/register`).**  

---

## Usage  

1️⃣ Open **`http://127.0.0.1:5000`** in your browser.  
2️⃣ **Register an account** (if not already registered).  
3️⃣ **Login** and access the **chatbot**.  
4️⃣ Type your message, and **Empathy AI** will respond!  

---


---

## Contributing  

Pull requests are welcome. For major changes, please open an **issue** first to discuss what you’d like to change.  

Make sure to update **documentation and tests** as appropriate.  

---

## License  

[MIT](https://choosealicense.com/licenses/mit/)  

---

## ⭐ Star the Repository!  

If you find this project helpful, please **⭐ star this repository** on GitHub! 🚀  



