#streamlit


import os
import requests
import streamlit as st
from main_rag import get_response

    
st.title("KIIT SOEE Chatbot")
st.info(
    "Ask me questions about KIIT school of electronics, its syllabus , about its curriculum,"
    "about the facilities, facuties and much more!"
)

if "messages" not in st.session_state:
    st.session_state.messages = []



for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if "output" in message.keys():
            st.markdown(message["output"])

        if "explanation" in message.keys():
            with st.status("How was this generated", state="complete"):
                st.info(message["explanation"])







if prompt := st.chat_input("What do you want to know?"):
    st.chat_message("user").markdown(prompt)

    st.session_state.messages.append({"role": "user", "output": prompt})

    
    data = {"text": prompt}

    with st.spinner("Searching for an answer..."):
        response = get_response(query=data) 
        if response != None:
            output_text = response
            explanation = "not yet done"

        else:
            output_text = """An error occurred while processing your message.
            Please try again or rephrase your message."""
            explanation = output_text

    st.chat_message("assistant").markdown(output_text)
    st.status("How was this generated", state="complete").info(explanation)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "output": output_text,
            "explanation": explanation,
        }
    )




