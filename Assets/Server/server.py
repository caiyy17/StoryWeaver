from flask import Flask, request, jsonify
import json
app = Flask(__name__)

import sys
from openai import OpenAI
from secrets_chatgpt import *
client = OpenAI(api_key=API_KEY)

def mock_chatgpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            # {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{prompt}"}
        ],
    )
    response = response.choices[0].message.content.strip()
    return response

def tts_openai(prompt):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=prompt
    )
    return response

def generate_image(prompt):
    response = null
    return "pass"


@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    prompt = data['prompt']
    answer = mock_chatgpt(prompt)

    # 将回答写入JSON文件
    with open('answer.json', 'w', encoding='utf-8') as file:
        json.dump({'prompt': prompt, 'answer': answer}, file, ensure_ascii=False)

    return "finished ask"

@app.route('/tts', methods=['POST'])
def tts():
    data = request.json
    prompt = data['prompt']
    audio = tts_openai(prompt)

    audio.stream_to_file('answer.mp3')
    return "finished tts"

@app.route('/image', methods=['POST'])
def image():
    data = request.json
    prompt = data['prompt']
    image = generate_image(prompt)

    return "finished image"

if __name__ == '__main__':
    app.run(debug=True, port=5050)