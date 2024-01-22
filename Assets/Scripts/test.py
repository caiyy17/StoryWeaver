import openai
from openai import OpenAI
client = OpenAI(api_key="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")

def askChatGPT(question):
    prompt = question
    completions = client.chat.completions.create(
        model="gpt-4",
        messages=[
            # {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{prompt}"}
        ],
    )
    message = completions.choices[0].message
    print(message)

askChatGPT("请告诉我中国的国土面积有多大")
print("Hello World!")