import sys
from openai import OpenAI
from secrets import *
client = OpenAI(api_key=API_KEY)

def askChatGPT(question):
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

if __name__ == "__main__":
    # first parameter is the question
    # read from the command line
    parameter = sys.argv[1]
    answer = askChatGPT(parameter)
    print(answer)
