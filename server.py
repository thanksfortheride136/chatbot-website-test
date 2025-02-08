from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import ollama

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")  # Serve index.html when accessing "/"

@app.route("/ask", methods=["POST"])
def ask():
    try:
        user_question = request.json.get("question", "")

        if not user_question:
            return jsonify({"error": "No question provided"}), 400

        response = ollama.chat(model="mistral", messages=[{"role": "user", "content": user_question}])

        return jsonify({"answer": response["message"]["content"]})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

