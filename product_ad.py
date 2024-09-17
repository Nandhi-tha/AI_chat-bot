#Product ad Generator
from openai import OpenAI
client = OpenAI()
from dotenv import load_dotenv
import os
load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

def advertisement():
  user_query = input("Enter your query:")
  chat_completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
        {
            "role": "system",
            "content": "Generate a creative advertisement for the product given by user."
        },
        {
            "role": "user",
            #"content": "Write a creative ad for the following product to run on Instagram:\n\"\"\"\"\"\"\nXR350 motorcycle for offroad and mountain riders. High performance 349cc engine. Available in 3 color segments. Customization available.\n\"\"\"\"\"\"\nThis is the ad I wrote for Instagram aimed at motorbiking lovers:\n\"\"\"\"\"\"",
            "content": f"{user_query}",
        }
    ],
    temperature=0.8,
    max_tokens=150,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\"\"\"\"\"\""]
  )
  
  output = chat_completion.choices[0].message
  print(output)


if __name__ == "__main__":
  advertisement()





