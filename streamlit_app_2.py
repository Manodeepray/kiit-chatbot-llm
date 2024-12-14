import os
import requests
import streamlit as st
from main_rag import get_response
from main_rag import gemini_response, chatbot_rag, ollama_response
import time

# App configuration and page layout
st.set_page_config(page_title="KIIT SOEE Chatbot", page_icon="🤖", layout="wide")

# Custom CSS to beautify the app
st.markdown("""
    <style>
        .title {
            font-size: 40px;
            color: #1E3A8A;
            text-align: center;
            margin-bottom: 20px;
        }
        .info-box {
            background-color: #E0F7FA;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        .chat-box {
            padding: 10px;
            margin-bottom: 10px;
        }
        .chat-input {
            border: 2px solid #1E88E5;
            padding: 10px;
            border-radius: 8px;
        }
        .spinner {
            margin-top: 20px;
        }
        .assistant-message {
            background-color: #E8F5E9;
            padding: 10px;
            border-radius: 8px;
            margin-top: 10px;
        }
        .user-message {
            background-color: #F3E5F5;
            padding: 10px;
            border-radius: 8px;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Title and introductory information
st.markdown('<h1 class="title">KIIT SOEE Chatbot</h1>', unsafe_allow_html=True)

# Welcome message / onboarding guide
if "welcome_shown" not in st.session_state:
    st.session_state.welcome_shown = True
    st.markdown(
        """
        <div style="background-color: #D1C4E9; padding: 20px; border-radius: 10px;">
            <h2>Welcome to the KIIT SOEE Chatbot! 🤖</h2>
            <p>I'm here to assist you with all your queries about the School of Electronics at KIIT.</p>
            <p>To get started, type your question below or choose a quick question!</p>
        </div>
        """, unsafe_allow_html=True
    )

# Quick action buttons / suggested questions
st.subheader("Quick Questions")
quick_questions = ["Curriculum Details", "Faculty Information", "Upcoming Events", "Facilities Overview"]
selected_question = st.radio("Or select a quick question to get started:", quick_questions)

if selected_question:
    prompt = selected_question

# Initialize messages if not already present
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages in a chat-like interface
with st.container():
    st.markdown("<h3>Conversation History</h3>", unsafe_allow_html=True)
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f'<div class="user-message">{message["output"]}</div>', unsafe_allow_html=True)
        elif message["role"] == "assistant":
            st.markdown(f'<div class="assistant-message">{message["output"]}</div>', unsafe_allow_html=True)
            if "explanation" in message:
                st.info(message["explanation"])

# Chatbot chain setup
chat_retriever_chain = chatbot_rag()

# Chat input area
if prompt := st.text_input("What do you want to know?", placeholder="Type your question here..."):
    st.session_state.messages.append({"role": "user", "output": prompt})

    # User message
    st.markdown(f'<div class="user-message">{prompt}</div>', unsafe_allow_html=True)
    # Typing indicator / loading animation
    with st.spinner("🤖 Typing..."):
        time.sleep(2)  # Simulate a delay for response generation
        response = None

        # Call the response generation function
        try:
            print("getting response from ollama")
            response = ollama_response(chat_retriever_chain=chat_retriever_chain, query=prompt)

        except Exception as e:
            print(f"error getting ollama response: {e}")
            
            
            
        if response is None:
            print(" getting response from gemini flash 1.5 ")
            try:
                response = gemini_response( chat_retriever_chain=chat_retriever_chain ,query=prompt)
            except Exception as e:
                print(f"error getting gemini response: {e}")
                
                
                
                
        documents = response if response else "An error occurred while processing your message. Please try again or rephrase your message."
        explanation = "Response generation details are not available yet."

    # Assistant message display
    st.markdown(f'<div class="assistant-message">{documents}</div>', unsafe_allow_html=True)

    # Store assistant response in session state
    st.session_state.messages.append(
        {
            "role": "assistant",
            "output": documents,
            "explanation": explanation,
        }
    )

# Persistent feedback mechanism
st.subheader("Was this response helpful?")
if st.button("👍 Yes"):
    st.success("Thank you for your feedback!")
if st.button("👎 No"):
    st.error("We'll work on improving our responses.")

# File upload / download capability
st.sidebar.header("File Operations")
uploaded_file = st.sidebar.file_uploader("Upload a file for analysis")
if uploaded_file is not None:
    st.sidebar.write("File uploaded successfully.")
st.sidebar.download_button("Download Guide", "This is a sample guide text.", file_name="guide.txt")

# User profile section
st.sidebar.markdown("### User Profile")
st.sidebar.text_input("Name", value="Guest User")
st.sidebar.text_input("Email")

# Help & support section
with st.expander("Need Help?"):
    st.write("You can ask me questions related to:")
    st.write("- Syllabus and Courses")
    st.write("- Faculty Information")
    st.write("- Events and Notifications")
