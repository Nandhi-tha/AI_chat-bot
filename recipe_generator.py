#Recipe Generator
from openai import OpenAI
client = OpenAI()
from dotenv import load_dotenv
import os
load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

def generate_recipe():
  user_query = input("Enter your query:")
  chat_completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
        {
            "role": "system",
            "content": "Give food recipe based on ingredients and instructions provided by the user."
        },
        {
            "role": "user",
            #"content": "Write a recipe based on these ingredients and instructions:\n\nCaramel Custard\n\nIngredients:\nMilk\nCustard Powder\n\nSugar\nMilkmaid\n\n Steps to be followed:",
            "content": f"{user_query}",
        }
    ],
    temperature=0,
    max_tokens=150,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.5
    )
  
  output = chat_completion.choices[0].message
  print(output)


if __name__ == "__main__":
  generate_recipe() 
