

# knowledge=open("knowledge.txt").read().lower()
# while True:
#     question=input("Customer: ").lower()

#     if question.lower() == "exit":
#         break

#     if "shipping" in question.lower():
#         start=knowledge.find("shipping")
#         print("Bot: ", knowledge[start:start+30])

#     elif "return" in question.lower():
#         start=knowledge.find("return")
#         print("Bot: ", knowledge[start:start+30])

#     elif "contact" in question.lower():
#         start=knowledge.find("contact")
#         print("Bot: ", knowledge[start:start+30])

#     else:
#         print("Bot: Sorry, I don't know.")

# --------------------------

# import requests

# while True:
#     question=input("You: ")

#     if question.lower() =="exit":
#         break

#     response=requests.post(
#         "http://localhost:11434/api/generate",
#         json={
#             "model": "qwen2.5:3b",
#             "prompt": question,
#             "stream": False
#         }
#     )

#     answer=response.json()["response"]
#     print("\nBot:", answer)
#     print()

# --------------Basic Ollama Streamlit------------

# import streamlit as st
# import requests

# with open("company_info.txt", "r", encoding="utf-8") as file:
#     company_info = file.read()

# st.title("ABC Fitness Gym Chatbot")

# question = st.text_input("Ask a question")

# if question:

#     prompt = f"""
# You are a customer support chatbot.

# Answer ONLY from the company information below.

# If the answer is not explicitly present in the company information, reply exactly:

# I don't have that information.

# Company Information:
# {company_info}

# Question:
# {question}
# """

#     response = requests.post(
#         "http://localhost:11434/api/generate",
#         json={
#             "model": "qwen2.5:7b",
#             "prompt": prompt,
#             "stream": False
#         }
#     )

#     answer = response.json()["response"]

#     if answer.strip() == "":
#         answer = "I don't have that information."

#     st.write("Bot:", answer)

# ------------------------

#     import streamlit as st
# st.title("Memory Test")
# if "counter" not in st.session_state:
#     st.session_state.counter = 0
# if st.button("Increase"):
#     st.session_state.counter += 1
# st.write("Count:", st.session_state.counter)

# --------------------

# import streamlit as st
# st.title("ABC Fitness Gym Chatbot")
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []
# message = st.text_input("Ask a question")
# if st.button("Send"):
#     st.session_state.chat_history.append(
#         "User: " + message
#     )
#     st.session_state.chat_history.append(
#         "Bot: This is a test response"
#     )
# for item in st.session_state.chat_history:
#     st.write(item)

# --------------------------------------Advance Ollama Streamlit No API-----------------------------------------



# import streamlit as st
# import requests

# # -----------------------
# # Page Configuration
# # -----------------------

# st.set_page_config(
#     page_title="ABC Fitness Gym Chatbot",
#     page_icon="🏋️",
#     layout="centered"
# )

# # -----------------------
# # Session Memory
# # -----------------------

# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# # -----------------------
# # Clear Chat
# # -----------------------

# if st.button("🗑️ Clear Chat"):
#     st.session_state.chat_history = []
#     st.rerun()

# # -----------------------
# # Company Information
# # -----------------------

# with open("company_info.txt", "r", encoding="utf-8") as file:
#     company_info = file.read()

# # -----------------------
# # Sidebar
# # -----------------------

# with st.sidebar:
#     st.header("Gym Information")
#     st.write("🏋️ ABC Fitness Gym")
#     st.write("📍 Kochi")
#     st.write("🕒 6 AM - 10 PM")
#     st.write("📞 9999999999")

# # -----------------------
# # Main Page
# # -----------------------

# st.title("🏋️ ABC Fitness Gym Chatbot")

# st.caption(
#     "Ask questions about memberships, trainers, timings and contact details."
# )

# # -----------------------
# # Display Chat History
# # -----------------------

# for item in st.session_state.chat_history:

#     if item.startswith("User:"):

#         with st.chat_message("user"):
#             st.write(item.replace("User: ", ""))

#     else:

#         with st.chat_message("assistant"):
#             st.write(item.replace("Bot: ", ""))

# # -----------------------
# # Chat Input
# # -----------------------

# message = st.chat_input("Ask a question")

# if message:

#     conversation = "\n".join(
#         st.session_state.chat_history
#     )

#     prompt = f"""
# You are a customer support chatbot.

# Answer ONLY from the company information below.

# If the answer is not explicitly present in the company information, reply exactly:

# I don't have that information.

# Company Information:
# {company_info}

# Previous Conversation:
# {conversation}

# Current Question:
# {message}
# """

#     with st.spinner("Thinking..."):

#         response = requests.post(
#             "http://localhost:11434/api/generate",
#             json={
#                 "model": "qwen2.5:7b",
#                 "prompt": prompt,
#                 "stream": False
#             }
#         )

#         answer = response.json()["response"]

#     if answer.strip() == "":
#         answer = "I don't have that information."

#     st.session_state.chat_history.append(
#         "User: " + message
#     )

#     st.session_state.chat_history.append(
#         "Bot: " + answer
#     )

#     st.rerun()

# ------------------API---------------

# from groq import Groq
# from dotenv import load_dotenv
# import os

# load_dotenv()

# client = Groq(
#     api_key=os.getenv("GROQ_API_KEY")
# )

# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     messages=[
#         {
#             "role": "user",
#             "content": "Explain machine learning in one sentence."
#         }
#     ]
# )

# print(response.choices[0].message.content)