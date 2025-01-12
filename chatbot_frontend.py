# Source: Below code is provided by Streamlit and AWS 

#1 import streamlit and chatbot file
import streamlit as st 
import chatbot_backend as demo

#2 Set Title for Chatbot
st.title("Hi, This is Chatbot Satish :sunglasses:")

#3 Initialize session state for memory
if 'memory' not in st.session_state:
    st.session_state.memory = demo.demo_memory()

#4 Initialize session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

#5 Re-render the chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["text"])

#6 Chat input and response handling
input_text = st.chat_input("Powered by Bedrock and Claude")
if input_text:
    # Display user message
    with st.chat_message("user"):
        st.markdown(input_text)
    
    # Add user message to chat history
    st.session_state.chat_history.append({
        "role": "user",
        "text": input_text
    })

    # Get assistant response
    assistant_response = demo.demo_conversation(
        input_text=input_text,
        memory=st.session_state.memory
    )
    
    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
    
    # Add assistant response to chat history
    st.session_state.chat_history.append({
        "role": "assistant",
        "text": assistant_response
    })
