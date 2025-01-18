import streamlit as st
import requests

def get_rasa_response(message):
    try:
        rasa_server_url = "http://localhost:5005/webhooks/rest/webhook"
        response = requests.post(
            rasa_server_url,
            json={"sender": "user", "message": message}
        )
        return [msg.get("text", "") for msg in response.json()]
    except requests.exceptions.RequestException:
        return ["Error: Could not connect to Rasa server"]

def on_chat_submit():
    st.info("what's up?")

def show_chatbot():
    # st.info("Bot: Hi there! How can I help you today?")
    # chat_input = st.chat_input("Chat with the bot")

    # if chat_input:
    #     on_chat_submit()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    prompt = st.chat_input("What's on your mind?")
    if prompt:
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        responses = get_rasa_response(prompt)
        with st.chat_message("assistant"):
            for response in responses:
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})