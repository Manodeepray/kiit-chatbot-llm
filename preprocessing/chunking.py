from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
import os
import pandas as pd

def load_csv_files(csv_files):
    data_frames = []
    
    for file in csv_files:
        if file.endswith('.csv'):
            csv_path = file
            df = pd.read_csv(csv_path)
            data_frames.append(df)
    
    combined_df = pd.concat(data_frames, ignore_index=True)
    combined_df = combined_df.dropna()
    combined_df = combined_df.reset_index(drop=True)
    return combined_df



def chunking_txt(txt_files):
    
    documents = []
    
    for file in txt_files:
        if file.endswith('.txt'):
            txt_path = file  # Use directory_path instead of txt_list
            with open(txt_path, 'r', encoding='utf-8') as f:
                content = f.read()
                documents.append(content)
    
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
    chunked_documents = text_splitter.split_documents(documents)
    
    return chunked_documents




def chunking_pdfs(pdfs_list):
    
    documents = []
    for file in pdfs_list:
        if file.endswith('.pdf'):
            pdf_path = file
            loader = PyPDFLoader(pdf_path)
            documents.extend(loader.load())
    
    
    
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
    chunked_documents = text_splitter.split_documents(documents)
    
    
    return chunked_documents


