import requests

while True:
    question=input("You: ")

    if question.lower() =="exit":
        break

    response=requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen2.5:3b",
            "prompt": question,
            "stream": False
        }
    )

    answer=response.json()["response"]
    print("\nBot:", answer)
    print()