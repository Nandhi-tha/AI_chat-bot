#meeting summarizer
from openai import OpenAI
client = OpenAI()
#api accessing
from dotenv import load_dotenv
import os
load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

def meeting_summary():
  user_query = input("Enter your query:")
  chat_completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
        {
            "role": "system",
            "content": "You will be provided with meeting notes, and your task is to summarize the meeting."
        },
        {
            "role": "user",
            "content": f"{user_query}",
        }
    ], 
    temperature=0.7,
    max_tokens=100,
    top_p=1
    )
  
  output = chat_completion.choices[0].message
  print(output)


if __name__ == "__main__":
  meeting_summary()
