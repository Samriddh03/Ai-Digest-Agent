import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

def generate_shorts(summary):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "AI Digest App"
    }

    payload = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [
            {
                "role": "user",
                "content": f"""
                Convert this into a 30-second YouTube Shorts script.
                Make it engaging, catchy, and viral:

                {summary}
                """
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        return f"Error: {response.status_code}"

    result = response.json()

    return result["choices"][0]["message"]["content"]