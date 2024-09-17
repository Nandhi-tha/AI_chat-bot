#SQL command generation
from openai import OpenAI
client = OpenAI()
#api accessing
from dotenv import load_dotenv
import os
load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

def sql_command_generation():
  user_query = input("Enter your query:")
  chat_completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
        {
            "role": "system",
            "content": "Generate SQL commands for the queries given by the user."
        },
        {
            "role": "user",
            #"content": "Write a query to find the count of employees in the ECE department.",
            "content": f"{user_query}",
        }
    ], 
    temperature=0.5,
    max_tokens=100,
    )
  
  output = chat_completion.choices[0].message
  print(output)


if __name__ == "__main__":
  sql_command_generation()
