import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen2.5:3b",
        "prompt": "What is 2+5?",
        "stream": False
    }
)

print(response.json()["response"])