import requests

with open("company_info.txt", "r", encoding="utf-8") as file:
    company_info=file.read()

chat_history=[]

while True:

    question=input("You: ")

    if question.lower() == "exit":
        break

    chat_history.append("User: " + question)

    conversation="\n".join(chat_history)
    prompt= f"""

    You are a customer support chatbot.

    Answer ONLY from the company information below.

    If the answer is not explicitly present in the company information, reply exactly:2

    I don't have that information.

    Company Information:   
    {company_info}

    Previous conversation:
    {conversation}

    Current Question:
    {question}

 """
    response=requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model" : "qwen2.5:7b",
            "prompt": prompt,
            "stream": False
         }
    )
    answer=response.json()["response"]

    if answer.strip()=="":
        answer="I don't have that information."
        
    chat_history.append("Bot: " + answer)


    print("\nBot: ",answer)
    print()