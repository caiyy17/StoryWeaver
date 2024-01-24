import sys
import requests
import json

answerPath = 'Assets/Scripts/answer.json'

def send_question(question):
    response = requests.post('http://127.0.0.1:5050/ask', json={'question': question})
    return response.json()

if __name__ == "__main__":
    # first parameter is the question
    # read from the command line
    if len(sys.argv) < 2:
        parameter = 'Hello'
    else:
        parameter = sys.argv[1]
    answer = send_question(parameter)
    with open(answerPath, 'w', encoding='utf-8') as file:
        json.dump(answer, file, ensure_ascii=False)
    print("Finished")