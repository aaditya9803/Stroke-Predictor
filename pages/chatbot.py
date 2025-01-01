import streamlit as st

def on_chat_submit():
    st.info("Bot: Hi there! How can I help you today?")

def show_chatbot():
    chat_input = st.chat_input("Chat with the bot")

    if chat_input:
        on_chat_submit()