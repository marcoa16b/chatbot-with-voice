import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY") 
openai.api_base = os.getenv("OPENAI_API_BASE_URL")

def getResponse(messages):
  res = openai.ChatCompletion.create(
    model="accounts/fireworks/models/llama-v2-7b-chat",
    messages=messages
  )
  return res.choices[0].message