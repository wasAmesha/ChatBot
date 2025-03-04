from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = print(os.environ["OPENAI_API_KEY"])

client = OpenAI()

## method 1

# response=client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     max_tokens=50,
#     n=1,
#     temperature=0,
#     messages=[
#         {"role":"user","content":"hello"}
#     ]
# )

# for choice in response.choices:
#     print(choice.message.content)

# print(response)


## method 2

# question = "hello"

# response=client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     max_tokens=50,
#     n=2,
#     temperature=0.8,
#     messages=[
#         {"role":"user","content": question}
#     ]
# )

# for choice in response.choices:
#     print(choice.message.content)


## method 3

# question = input("User: ")

# response=client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     max_tokens=50,
#     n=1,
#     temperature=0,
#     messages=[
#         {"role":"user","content": question}
#     ]
# )

# for choice in response.choices:
#     print(f"AI: {choice.message.content}")


## method 4

while True:
    question = input("User: ")
    if question != "bye":

        response=client.chat.completions.create(
            model="gpt-3.5-turbo",
            max_tokens=50,
            n=1,
            temperature=0.3,
            messages=[
                {"role":"user","content": question}
            ]
        )

        for choice in response.choices:
            print(f"AI: {choice.message.content}")
    else:
            print("AI: Bye...")
            break
