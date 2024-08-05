import lister
from preprocessing.chunking import *
from langchain.vectorstores import Chroma
import chromadb
from embedding import *
import faiss
import numpy as np
from langchain_community.document_loaders.csv_loader import CSVLoader








def load_db_chunk_persist_txt(txt_files , embedding):
    
    chunked_documents = chunking_txt(txt_files)
    client = chromadb.Client()
    if client.list_collections():
        consent_collection = client.create_collection("consent_collection")
    else:
        print("Collection already exists")
    
   
    
    if embedding == "hf":
        hf = hugging_face_embeddding()
        vectordb_txt = Chroma.from_documents(
            documents=chunked_documents,
            embedding=hf,
            persist_directory="artifacts"
        )
    elif embedding == "sentence_tf":
        embedding_function = sebtence_transformer_embedding()
        vectordb_txt = Chroma.from_documents(
            documents=chunked_documents,
            embedding=embedding_function,
            persist_directory="artifacts"
        )
    vectordb_txt.persist()
    return vectordb_txt

def load_db_chunk_persist_pdf(pdf_files , embedding):
    
    chunked_documents = chunking_pdfs(pdf_files)
    client = chromadb.Client()
    if client.list_collections():
        consent_collection = client.create_collection("consent_collection")
    else:
        print("Collection already exists")
    
   
    
    if embedding == "hf":
        hf = hugging_face_embeddding()
        vectordb_pdf = Chroma.from_documents(
            documents=chunked_documents,
            embedding=hf,
            persist_directory="artifacts"
        )
    elif embedding == "sentence_tf":
        embedding_function = sebtence_transformer_embedding()
        vectordb_pdf = Chroma.from_documents(
            documents=chunked_documents,
            embedding=embedding_function,
            persist_directory="artifacts"
        )
    vectordb_pdf.persist()
    return vectordb_pdf




def load_db_persist_csv(csv_files, embedding):
    df = load_csv_files(csv_files)
    csv_path = "src/csv/combined.csv" 
    df.to_csv(csv_path)

    loader = CSVLoader(file_path=csv_path)
    documents = loader.load()
    
    client = chromadb.Client()
    if client.list_collections():
        consent_collection = client.create_collection("consent_collection")
    else:
        print("Collection already exists")
    
   
    
    if embedding == "hf":
        hf = hugging_face_embeddding()
        vector_db_csv = Chroma.from_documents(
            documents=documents,
            embedding=hf,
            persist_directory="artifacts"
        )
    elif embedding == "sentence_tf":
        embedding_function = sebtence_transformer_embedding()
        vector_db_csv = Chroma.from_documents(
            documents=documents,
            embedding=embedding_function,
            persist_directory="artifacts"
        )
    vector_db_csv.persist()
    return vector_db_csv









####################################################################################################################

if __name__ == "__main__":
    path = 'src\data'
    txt_files,csv_files,pdf_files  = lister.find_files(path)
    embedding = "hf"
    vector_db_pdf = load_db_chunk_persist_pdf(pdf_files,embedding)
    vector_db_txt = load_db_chunk_persist_txt(txt_files,embedding)
    vector_db_csv = load_db_persist_csv(csv_files,embedding)
