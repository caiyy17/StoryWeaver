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
    message = completions.choices[0].message.content.strip()
    return message

answer = askChatGPT("Please reply that is a test")
print(answer)