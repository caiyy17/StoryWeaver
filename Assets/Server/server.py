from flask import Flask, request, jsonify
import json
app = Flask(__name__)

import sys
from openai import OpenAI
from secrets_chatgpt import *
client = OpenAI(api_key=API_KEY)

def mock_chatgpt(question):
    prompt = question
    completions = client.chat.completions.create(
        model="gpt-4",
        messages=[
            # {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{prompt}"}
        ],
    )
    message = completions.choices[0].message.content.strip()
    return message

def tts_openai(text):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    return response

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data['question']
    answer = mock_chatgpt(question)
    audio = tts_openai(answer)

    # 将回答写入JSON文件
    with open('answer.json', 'w', encoding='utf-8') as file:
        json.dump({'question': question, 'answer': answer}, file, ensure_ascii=False)
    audio.stream_to_file('answer.mp3')

    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True, port=5050)