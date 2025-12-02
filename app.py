import streamlit as st
import nltk
from nltk.chat.util import Chat, reflections

import nltk
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

# Chatbot pairs
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today? 😊"]
    ],
    [
        r"what is your name?",
        ["I'm SmartAssist, your personal AI chatbot! 🤖"]
    ],
    [
        r"how are you ?",
        ["I'm doing great! Thanks for asking. How about you?"]
    ],
    [
        r"(.*) your favourite programming language?",
        ["Definitely Python! Simple, powerful, and perfect for beginners. 🐍"]
    ],
    [
        r"(.*)",
        ["I'm still learning. Could you rephrase that? 🙂"]
    ],
]

chat = Chat(pairs, reflections)

# --- Streamlit UI ---
st.set_page_config(page_title="SmartAssist – AI Chatbot", page_icon="🤖")

st.markdown(
    """
    <h1 style="text-align:center; color:#4CAF50;">🤖 SmartAssist AI Chatbot</h1>
    <p style="text-align:center;">Built with Python & NLP • Clean UI • Beginner Friendly</p>
    <hr>
    """,
    unsafe_allow_html=True
)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat Display
for msg, sender in st.session_state.messages:
    if sender == "user":
        st.markdown(f"<div style='text-align: right; color: white; background:#4CAF50; padding:10px; margin:5px; border-radius:10px; display:inline-block;'>{msg}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='text-align: left; background:#E8E8E8; padding:10px; margin:5px; border-radius:10px; display:inline-block;'>{msg}</div>", unsafe_allow_html=True)

# Input Box
user_input = st.text_input("Type your message here:", "")

# Process reply
if user_input:
    bot_reply = chat.respond(user_input)

    st.session_state.messages.append((user_input, "user"))
    st.session_state.messages.append((bot_reply, "bot"))

    st.rerun()