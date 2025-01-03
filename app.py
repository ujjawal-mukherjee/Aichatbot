import os
import nltk
from flask import Flask, render_template, request, jsonify
from chat import get_response  # Import from chat.py

# Ensure necessary NLTK resources are downloaded
nltk.download('punkt')  # Ensure the 'punkt' tokenizer is downloaded
nltk.download('punkt_tab')  # Try downloading punkt_tab if necessary

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"response": "Please enter a message."})
    
    bot_response = get_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Ensure the correct port for Render
    app.run(host="0.0.0.0", port=port)
