
import requests

def call_llm(prompt, model="llama3"):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False,
            "temperature": 0.3
        }
    )

    return response.json()["response"]