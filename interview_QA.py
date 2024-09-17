#Interview question and answer
from openai import OpenAI
client = OpenAI()
from dotenv import load_dotenv
import os
load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

def QA_interview():
  user_query = input("Enter your query:")
  chat_completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
        {
            "role": "system",
            "content": "Generate interview questions with answers based on role provided by user."
        },
        {
            "role": "user",
            #"content": "Generate a list of questions for my interview with data scientist:\n\n1.",
            "content": f"{user_query}",

        }
    ],
    temperature=0.5,
    max_tokens=200,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n\n"]
    )
  
  output = chat_completion.choices[0].message
  print(output)


if __name__ == "__main__":
  QA_interview()