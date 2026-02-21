import os
from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Render Environment kısmına eklediğin GEMINI_API_KEY'i kullanır
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

@app.route('/')
def home():
    return "Dilekçe Matik Python Sunucusu Aktif! 🚀"

@app.route('/generate-dilekce', methods=['POST'])
def generate_dilekce():
    try:
        data = request.json
        prompt_text = data.get('prompt')
        
        # Yapay zeka modelini çağırıyoruz
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        response = model.generate_content(prompt_text)
        
        return jsonify({"dilekce": response.text})
    except Exception as e:
        print(f"Hata oluştu: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Render'ın beklediği port ayarı
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)