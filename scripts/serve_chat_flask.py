import html
import json
import os

from dotenv import load_dotenv
from flask import Flask, render_template, jsonify

load_dotenv()

app = Flask(__name__)


# Route pour servir le fichier HTML
@app.route("/")
def index():
    chat_html = os.getenv("CHAT-HTML")
    return render_template(chat_html)


# Route pour servir le fichier JSON en échappant les fragments HTML
@app.route("/get_json")
def get_json():
    static_conversations_json = os.getenv("STATIC-CONVERSATIONS-JSON")
    with open(static_conversations_json, "r", encoding="utf-8") as json_file:
        json_data = json.load(json_file)

    # Fonction récursive pour échapper tous les fragments HTML dans les valeurs du JSON
    def escape_html_in_json(data):
        if isinstance(data, dict):
            return {key: escape_html_in_json(value) for key, value in data.items()}
        elif isinstance(data, list):
            return [escape_html_in_json(element) for element in data]
        elif isinstance(data, str):
            return html.escape(data)
        else:
            return data

    escaped_json_data = escape_html_in_json(json_data)

    return jsonify(escaped_json_data)


if __name__ == "__main__":
    app.run(debug=True)
