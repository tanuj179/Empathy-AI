document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("chatbox").innerHTML = ""; // Clear chat on refresh
});

function sendMessage() {
    let userMessage = document.getElementById("userInput").value.trim();
    let chatbox = document.getElementById("chatbox");

    if (userMessage === "") {
        alert("❌ Please enter a message.");
        return;
    }

    // Show user message in chatbox
    let userMsg = document.createElement("div");
    userMsg.classList.add("user-msg");
    userMsg.innerHTML = `<b>You:</b> ${userMessage}`;
    chatbox.appendChild(userMsg);

    fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userMessage }),
    })
    .then(response => response.json())
    .then(data => {
        let botMsg = document.createElement("div");
        botMsg.classList.add("bot-msg");

        // Properly format new lines in response
        botMsg.innerHTML = `<b>Empathy AI:</b> ${data.response.replace(/\n/g, "<br>")}`;

        chatbox.appendChild(botMsg);
        chatbox.scrollTop = chatbox.scrollHeight; // Auto-scroll
    })
    .catch(() => {
        let errorMsg = document.createElement("div");
        errorMsg.classList.add("error-msg");
        errorMsg.innerText = "❌ Error: Unable to get a response.";
        chatbox.appendChild(errorMsg);
    });

    document.getElementById("userInput").value = "";
}
