import os
from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Bağlantıyı en stabil hale getiriyoruz
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"), transport='rest')

@app.route('/')
def home():
    return "Sunucu Calisiyor!"

@app.route('/generate-dilekce', methods=['POST'])
def generate_dilekce():
    try:
        data = request.json
        prompt_text = data.get('prompt')

        # Model ismini en standart haliyle deniyoruz
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt_text)

        return jsonify({"dilekce": response.text})
    except Exception as e:
        print(f"Hata: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)