#general chat bot
from openai import OpenAI
client = OpenAI()

from dotenv import load_dotenv
import os
load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

def chat_bot():
  user_query = input("Enter your query:")
  chat_completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
        {
            "role": "system",
            "content": "Respond to all types of user queries."
        },
        {
            "role": "user",
            "content": f"{user_query}",
        }
    ], 
    temperature=0.5,
    max_tokens=200,
    top_p=1
    )
  
  output = chat_completion.choices[0].message
  print(output)


if __name__ == "__main__":
  chat_bot()


