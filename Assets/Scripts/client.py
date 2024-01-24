import sys
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

if __name__ == "__main__":
    # first parameter is the question
    # read from the command line
    if len(sys.argv) < 3:
        prompt = 'Hello'
        answer = send_question(prompt, 1)
    elif sys.argv[1] == "ask":
        prompt = sys.argv[2]
        answer = send_question(prompt)
    elif sys.argv[1] == "tts":
        prompt = sys.argv[2]
        answer = tts(prompt)
    elif sys.argv[1] == "image":
        prompt = sys.argv[2]
        answer = generate_image(prompt)
    else:
        answer = "unknown task"

    print(answer)