#Information extraction
from openai import OpenAI
client = OpenAI()
from dotenv import load_dotenv
import os
load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

def extract_info():
  user_query = input("Enter your query:")
  chat_completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
        {
            "role": "system",
            "content": "Extract information from the passage provided by the user."
        },
        {
            "role": "user",
            #"content": "Someone asked me to extract information from this passage:\n\"\"\"\nGenerative Pre-trained Transformer 3 (GPT-3) is an autoregressive language model that uses deep learning to produce human-like text. It is the third-generation language prediction model in the GPT-n series (and the successor to GPT-2) created by OpenAI, a San Francisco-based artificial intelligence research laboratory.[2] GPT-3's full version has a capacity of 175 billion machine learning parameters. GPT-3, which was introduced in May 2020, and was in beta testing as of July 2020,[3] is part of a trend in natural language processing (NLP) systems of pre-trained language representations.[1] Before the release of GPT-3, the largest language model was Microsoft's Turing NLG, introduced in February 2020, with a capacity of 17 billion parameters or less than a tenth of GPT-3s.[4]\n\"\"\"\nI noted down few points after reading the passage:\n\"\"\"\n",
            "content": f"{user_query}",
        }
    ], 
    temperature=0.3,
    max_tokens=150,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\"\"\""]
    )
  
  output = chat_completion.choices[0].message
  print(output)


if __name__ == "__main__":
  extract_info()
