import openai

client = openai.OpenAI(api_key="")

userText = input("What can ChatGOT do for you today?")

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": userText,
        }
    ],
    model="gpt-4o",
)

print(chat_completion.choices[0].message.content)