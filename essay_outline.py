#Essay outline 
from openai import OpenAI
client = OpenAI()
from dotenv import load_dotenv
import os
load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

def essay_writer():
  user_query = input("Enter your query:")
  chat_completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
        {
            "role": "system",
            "content": "Write an essay."
        },
        {
            "role": "user",
            #"content": "Create an outline for an essay about Metallica and their contribution to metal music:\n\nI: Introduction",
            "content": f"{user_query}",
        }
    ],
    temperature=0.7,
    max_tokens=150,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )
  
  output = chat_completion.choices[0].message
  print(output)


if __name__ == "__main__":
  essay_writer()
  
