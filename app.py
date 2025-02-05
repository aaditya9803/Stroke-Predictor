import streamlit as st
import requests

# Page config
st.set_page_config(
    page_title="Rasa Chatbot",
    page_icon="🤖"
)

# Title
st.title("Chat with Rasa Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Your message"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Send user message to Rasa and get response
    response = requests.post(
        url="http://localhost:5005/webhooks/rest/webhook",
        json={"sender": "user", "message": prompt}
    )
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        if response.status_code == 200:
            rasa_response = response.json()
            if rasa_response:
                bot_message = rasa_response[0].get("text", "Sorry, I didn't understand that.")
            else:
                bot_message = "I received your message but I'm not sure how to respond."
        else:
            bot_message = "Sorry, I'm having trouble connecting to the server."
        
        st.markdown(bot_message)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": bot_message})