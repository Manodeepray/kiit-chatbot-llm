import streamlit as st
import os
from main_rag import gemini_response , chatbot_rag , ollama_response , hf_response
import vector_db

import asyncio

# Chatbot UI
st.title("Streamlit Chatbot")

# Initialize session state for conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input for user query
user_input = st.chat_input("Enter your query:")


PDF_FOLDER = "./src/data/uploaded_pdfs"
CSV_FOLDER = "./src/data/uploaded_csvs"
TXT_FOLDER = "./src/data/uploaded_txts"

# Ensure directories exist
for folder in [PDF_FOLDER, CSV_FOLDER, TXT_FOLDER]:
    os.makedirs(folder, exist_ok=True)

# Sidebar for file upload
st.sidebar.title("Upload Files")
file = st.sidebar.file_uploader("Choose a file", type=["pdf", "csv", "txt"])

# Variable to track file path
file_path = None


async def save_file(file , file_path):
    
    with open(file_path, "wb") as f:
        await asyncio.to_thread(f.write, file.getbuffer())
    return file_path
    


# Auto-save uploaded file
if file:
    file_type = file.type
    file_name = file.name

    if file_type == "application/pdf":
        file_path = os.path.join(PDF_FOLDER, file_name)
    elif file_type == "text/csv":
        file_path = os.path.join(CSV_FOLDER, file_name)
    elif file_type == "text/plain":
        file_path = os.path.join(TXT_FOLDER, file_name)
    else:
        st.sidebar.error("Unsupported file format")
        file_path = None

    if file_path:
        # Save file
        file_path = asyncio.run(save_file(file, file_path))
        st.sidebar.success(f"File saved to {file_path} ✅")



async def process_vector_db():
    """creates vectorstore  """
    try:
        await asyncio.to_thread(vector_db.load_and_save_Vector_stores)
        st.sidebar.success("File processed and stored successfully! 🎉")
    except Exception as e:
        st.sidebar.error(f"Processing error: {str(e)} ❌")


# Button to trigger Vector Store Processing
if file_path:
    if st.sidebar.button("Process & Save to Vector Store"):
        with st.spinner("Processing file..."):
           asyncio.run(process_vector_db())

# Dropdown for file selection
st.sidebar.title("Select File Type")
file_type_selected = st.sidebar.selectbox("Choose file type", ["PDF", "CSV", "TXT"])

# Load selected files
if file_type_selected == "PDF":
    folder = PDF_FOLDER
elif file_type_selected == "CSV":
    folder = CSV_FOLDER
elif file_type_selected == "TXT":
    folder = TXT_FOLDER

# Show available files
st.sidebar.write("Available files:")
files = os.listdir(folder)
selected_file = st.sidebar.selectbox("Choose a file", files) if files else None














st.sidebar.title("Select Action")
action_selected = st.sidebar.selectbox("Choose a LLm service", ["Local Ollama", "Gemini API" , "HuggingFace API"])





async def get_chat_retriever_chain(action_selected):
    """Asynchronously initialize the chat retriever chain."""
    if action_selected == "Local Ollama":
        return await asyncio.to_thread(chatbot_rag, mode='OLLAMA')
    elif action_selected == "Gemini API":
        return await asyncio.to_thread(chatbot_rag, mode='GEMINI')
    elif action_selected == "HuggingFace API":
        return await asyncio.to_thread(chatbot_rag, mode='HF')
    


chat_retriever_chain = asyncio.run(get_chat_retriever_chain(action_selected))


async def get_chatbot_response(action_selected, query):
    """Asynchronously fetch chatbot response."""
    if action_selected == "Local Ollama":
        return await asyncio.to_thread(ollama_response, chat_retriever_chain, query)
    elif action_selected == "Gemini API":
        return await asyncio.to_thread(gemini_response, chat_retriever_chain, query)
    elif action_selected == "HuggingFace API":
        return await asyncio.to_thread(hf_response, chat_retriever_chain, query)

if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = asyncio.run(get_chatbot_response(action_selected, user_input))
    
    # Generate and display bot response
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
