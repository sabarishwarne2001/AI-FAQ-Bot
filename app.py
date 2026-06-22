import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

groq_api_key= os.getenv("GROQ_API_KEY")

if not groq_api_key:
    groq_api_key=st.secrets("GROQ_API_KEY")

client=Groq(api_key=groq_api_key)

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

    st.header("🏋️ ABC Fitness Gym")

    st.write("📍 Kochi, Kerala")
    st.write("🕒 5 AM - 11 PM")
    st.write("📞 +91 99999 99999")
    st.write("📧 contact@abcfitnessgym.com")

    st.divider()

    st.subheader("Services")

    st.write("✅ Gym Access")
    st.write("✅ Personal Training")
    st.write("✅ Yoga")
    st.write("✅ Zumba")
    st.write("✅ Nutrition Guidance")

# -----------------------
# Main Page
# -----------------------

st.title("🏋️ ABC Fitness Gym Chatbot")

st.caption(
    "Ask questions about memberships, trainers, timings and contact details."
)

st.markdown("""
### Example Questions

- What membership plans are available?
- Do you offer personal training?
- Who are the trainers?
- Do you provide diet consultation?
- What are the gym timings?
- Is there a free trial?
""")

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

    messages = [
    {
        "role": "system",
        "content": f"""
You are a customer support chatbot.

Answer ONLY from the company information below.

If the answer is not explicitly present in the company information, reply exactly:

I don't have that information.

Company Information:
{company_info}
"""
    },
    {
        "role": "user",
        "content": f"""
Previous Conversation:
{conversation}

Current Question:
{message}
"""
    }
]

    with st.spinner("Thinking..."):

      response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.3
    )

    answer = response.choices[0].message.content

    if answer.strip() == "":
        answer = "I don't have that information."

    st.session_state.chat_history.append(
        "User: " + message
    )

    st.session_state.chat_history.append(
        "Bot: " + answer
    )

    st.rerun()