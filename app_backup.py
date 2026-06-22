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



#     import streamlit as st
# st.title("Memory Test")
# if "counter" not in st.session_state:
#     st.session_state.counter = 0
# if st.button("Increase"):
#     st.session_state.counter += 1
# st.write("Count:", st.session_state.counter)



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