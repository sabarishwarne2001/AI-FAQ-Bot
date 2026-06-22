knowledge=open("knowledge.txt").read().lower()
while True:
    question=input("Customer: ").lower()

    if question.lower() == "exit":
        break

    if "shipping" in question.lower():
        start=knowledge.find("shipping")
        print("Bot: ", knowledge[start:start+30])

    elif "return" in question.lower():
        start=knowledge.find("return")
        print("Bot: ", knowledge[start:start+30])

    elif "contact" in question.lower():
        start=knowledge.find("contact")
        print("Bot: ", knowledge[start:start+30])

    else:
        print("Bot: Sorry, I don't know.")
