from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
openai.api_key = os.getenv("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")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json.get("message")
    
    if not user_message:
        return jsonify({"error": "Empty message"}), 400
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are OAI, a helpful AI assistant."},
                      {"role": "user", "content": user_message}]
        )
        reply = response["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
