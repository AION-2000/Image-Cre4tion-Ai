from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

OPENAI_API_KEY = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-image', methods=['POST'])
def generate_image():
    data = request.json
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    url = "https://api.openai.com/v1/images/generations"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "dall-e-3",
        "prompt": prompt,
        "n": 1,
        "size": "512x512"
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        image_url = response.json()['data'][0]['url']
        return jsonify({"image_url": image_url})
    else:
        return jsonify({"error": "Failed to generate image"}), 500

if __name__ == "__main__":
    app.run(debug=True)

print(f"Using API key: {OPENAI_API_KEY[:5]}...")  # just first 5 chars for safety
