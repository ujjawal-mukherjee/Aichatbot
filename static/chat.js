const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");

sendBtn.addEventListener("click", () => {
    const message = userInput.value;
    if (!message) return;

    appendMessage("You", message);
    userInput.value = "";

    fetch("/chat", {
        method: "POST",
        body: JSON.stringify({ message }),
        headers: {
            "Content-Type": "application/json"
        }
    })
        .then(response => response.json())
        .then(data => appendMessage("Bot", data.response))
        .catch(error => console.error("Error:", error));
});

function appendMessage(sender, message) {
    const msgDiv = document.createElement("div");
    msgDiv.textContent = `${sender}: ${message}`;
    chatBox.appendChild(msgDiv);
}
