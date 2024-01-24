import sys
import json
import requests

def send_question(prompt, id = 0):
    response = requests.post('http://127.0.0.1:5050/ask', json={'prompt': prompt, 'id': id})
    return response.json()

def tts(prompt):
    response = requests.post('http://127.0.0.1:5050/tts', json={'prompt': prompt})
    return response.json()

def generate_image(prompt):
    response = requests.post('http://127.0.0.1:5050/image', json={'prompt': prompt})
    return response.json()

def parse(prompt):
    response = requests.post('http://127.0.0.1:5050/parse', json={'prompt': prompt})
    return response.json()

if __name__ == "__main__":
    # first parameter is the question
    # read from the command line
    if len(sys.argv) < 2:
        # prompt = "Hello"
        # answer = send_question(prompt, 999)
        with open(f"Assets/Server/answer.json", 'r', encoding='utf-8') as file:
            temp = json.load(file)
        prompt = temp["answer"]
        print(prompt)
        answer = parse(prompt)
    elif sys.argv[1] == "ask":
        prompt = sys.argv[2]
        id = sys.argv[3]
        answer = send_question(prompt, id)
    elif sys.argv[1] == "tts":
        prompt = sys.argv[2]
        answer = tts(prompt)
    elif sys.argv[1] == "image":
        prompt = sys.argv[2]
        answer = generate_image(prompt)
    elif sys.argv[1] == "parse":
        with open(f"Assets/Server/answer.json", 'r', encoding='utf-8') as file:
            temp = json.load(file)
        prompt = temp["answer"]
        answer = parse(prompt)
    else:
        answer = "unknown task"

    print(answer)