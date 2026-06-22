import streamlit as st
import requests

# -----------------------
# Page Configuration
# -----------------------

st.set_page_config(
    page_title="ABC Fitness Gym Chatbot",
    page_icon="🏋️",
    layout="centered"
)

# -----------------------
# Session Memory
# -----------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -----------------------
# Clear Chat
# -----------------------

if st.button("🗑️ Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()

# -----------------------
# Company Information
# -----------------------

with open("company_info.txt", "r", encoding="utf-8") as file:
    company_info = file.read()

# -----------------------
# Sidebar
# -----------------------

with st.sidebar:
    st.header("Gym Information")
    st.write("🏋️ ABC Fitness Gym")
    st.write("📍 Kochi")
    st.write("🕒 6 AM - 10 PM")
    st.write("📞 9999999999")

# -----------------------
# Main Page
# -----------------------

st.title("🏋️ ABC Fitness Gym Chatbot")

st.caption(
    "Ask questions about memberships, trainers, timings and contact details."
)

# -----------------------
# Display Chat History
# -----------------------

for item in st.session_state.chat_history:

    if item.startswith("User:"):

        with st.chat_message("user"):
            st.write(item.replace("User: ", ""))

    else:

        with st.chat_message("assistant"):
            st.write(item.replace("Bot: ", ""))

# -----------------------
# Chat Input
# -----------------------

message = st.chat_input("Ask a question")

if message:

    conversation = "\n".join(
        st.session_state.chat_history
    )

    prompt = f"""
You are a customer support chatbot.

Answer ONLY from the company information below.

If the answer is not explicitly present in the company information, reply exactly:

I don't have that information.

Company Information:
{company_info}

Previous Conversation:
{conversation}

Current Question:
{message}
"""

    with st.spinner("Thinking..."):

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "qwen2.5:7b",
                "prompt": prompt,
                "stream": False
            }
        )

        answer = response.json()["response"]

    if answer.strip() == "":
        answer = "I don't have that information."

    st.session_state.chat_history.append(
        "User: " + message
    )

    st.session_state.chat_history.append(
        "Bot: " + answer
    )

    st.rerun()