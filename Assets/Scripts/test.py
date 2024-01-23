import sys
import requests
import json

def send_question(question):
    response = requests.post('http://127.0.0.1:5000/ask', json={'question': question})
    return response.json()

if __name__ == "__main__":
    # first parameter is the question
    # read from the command line
    parameter = sys.argv[1]
    answer = send_question(parameter)
    print(answer['answer'])