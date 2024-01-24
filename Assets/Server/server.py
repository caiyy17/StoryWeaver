from flask import Flask, request, jsonify
import json
app = Flask(__name__)

import sys
import os
import requests
import base64
from io import BytesIO
from PIL import Image

from openai import OpenAI
from secrets_chatgpt import *
client = OpenAI(api_key=API_KEY)

def mock_chatgpt(prompt, id=0):
    if os.path.exists(f"history_{id}.json"):
        with open(f"history_{id}.json", 'r', encoding='utf-8') as file:
            history = json.load(file)
    else:
        history = [{"role": "system", "content": "You are a helpful assistant."}]
    history.append({"role": "user", "content": f"{prompt}"})
    response = client.chat.completions.create(
        model="gpt-4",
        messages=history
    )
    response = response.choices[0].message.content.strip()
    history.append({"role": "assistant", "content": f"{response}"})
    with open(f"history_{id}.json", 'w', encoding='utf-8') as file:
        json.dump(history, file, ensure_ascii=False)
    return response

def tts_openai(prompt):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=prompt
    )
    return response

def generate_image(prompt):
    response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1,
    response_format = "b64_json"
    )
    image = response.data[0].b64_json
    return image

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    prompt = data['prompt']
    answer = mock_chatgpt(prompt)

    # 将回答写入JSON文件
    with open('answer.json', 'w', encoding='utf-8') as file:
        json.dump({'prompt': prompt, 'answer': answer}, file, ensure_ascii=False)

    return jsonify({'answer': "finished ask"})

@app.route('/tts', methods=['POST'])
def tts():
    data = request.json
    prompt = data['prompt']
    audio = tts_openai(prompt)

    audio.stream_to_file('answer.mp3')
    return jsonify({'answer': "finished tts"})

@app.route('/image', methods=['POST'])
def image():
    data = request.json
    prompt = data['prompt']
    image = generate_image(prompt)
    image = base64.b64decode(image)
    image = Image.open(BytesIO(image))
    image.save('answer.png')

    return jsonify({'answer': "finished image"})

if __name__ == '__main__':
    app.run(debug=True, port=5050)