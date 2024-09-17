#meeting summarizer
from openai import OpenAI
client = OpenAI()
#api accessing
from dotenv import load_dotenv
import os
load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

def resume_generator():
  user_query = input("Enter your query:")
  chat_completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
        {
            "role": "system",
            "content": "Generate a Resume from the paragraph about experience and skillset provided by user"
        },
        {
            "role": "user",
            "content": f"{user_query}",
        }
    ], 
    temperature=0.8,
    max_tokens=150,
    top_p=1
    )
  
  output = chat_completion.choices[0].message
  print(output)


if __name__ == "__main__":
  resume_generator()
