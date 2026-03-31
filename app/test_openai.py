import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("DEBUG KEY:", os.getenv("OPENAI_API_KEY"))  # optional debug

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Say hello"}]
)

print(response.choices[0].message.content)