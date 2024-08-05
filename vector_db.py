from rag import lister
from preprocessing import chunking
from langchain.vectorstores import Chroma
import chromadb
from rag import embedding
import faiss
import numpy as np
from langchain_community.document_loaders.csv_loader import CSVLoader
import  os
import sys





def load_db_chunk_persist_txt(txt_files , embeddings):
    
    chunked_documents = chunking.chunking_txt(txt_files)
    client = chromadb.Client()
    if client.list_collections():
        consent_collection = client.create_collection("consent_collection")
    else:
        print("Collection already exists")
    
   
    
    if embeddings == "hf":
        hf = embedding.hugging_face_embeddding()
        vectordb_txt = Chroma.from_documents(
            documents=chunked_documents,
            embedding=hf,
            persist_directory="artifacts"
        )
        print("\n vector_txt_db loaded successfully")

    elif embeddings == "sentence_tf":
        embedding_function = embedding.sentence_transformer_embedding()
        vectordb_txt = Chroma.from_documents(
            documents=chunked_documents,
            embedding=embedding_function,
            persist_directory="artifacts"
        )
        print("\n vector_txt_db loaded successfully")

    vectordb_txt.persist()
    print("\n vector_txt_db persisted successfully")

    return vectordb_txt

def load_db_chunk_persist_pdf(pdf_files , embeddings):
    
    chunked_documents = chunking.chunking_pdfs(pdf_files)
    client = chromadb.Client()
    if client.list_collections():
        consent_collection = client.create_collection("consent_collection")
    else:
        print("Collection already exists")
    
   
    
    if embeddings == "hf":
        hf = embedding.hugging_face_embeddding()
        
        vectordb_pdf = Chroma.from_documents(
            documents=chunked_documents,
            embedding=hf,
            persist_directory="artifacts"
        )
        print("\n vector_pdf_db loaded successfully")

    elif embeddings == "sentence_tf":
        embedding_function = embedding.sentence_transformer_embedding()
        vectordb_pdf = Chroma.from_documents(
            documents=chunked_documents,
            embedding=embedding_function,
            persist_directory="artifacts"
        )
        print("\n vector_pdf_db loaded successfully")

    vectordb_pdf.persist()
    print("\n vector_pdf_db persisted successfully")

    return vectordb_pdf




def load_db_persist_csv(csv_files, embeddings):
    df = chunking.load_csv_files(csv_files)
    csv_path = "src/csv/combined.csv" 
    df.to_csv(csv_path)

    loader = CSVLoader(file_path=csv_path)
    documents = loader.load()
    
    client = chromadb.Client()
    if client.list_collections():
        consent_collection = client.create_collection("consent_collection")
    else:
        print("Collection already exists")
    
   
    
    if embeddings == "hf":
        hf = embedding.hugging_face_embeddding()
        vector_db_csv = Chroma.from_documents(
            documents=documents,
            embedding=hf,
            persist_directory="artifacts"
        )
        print("\n vector_csv_db loaded successfully")

    elif embeddings == "sentence_tf":
        embedding_function = embedding.sentence_transformer_embedding()
        vector_db_csv = Chroma.from_documents(
            documents=documents,
            embedding=embedding_function,
            persist_directory="artifacts"
        )
        print("\n vector_csv_db loaded successfully")

    vector_db_csv.persist()
    print("\n vector_csv_db persisted successfully")

    return vector_db_csv









####################################################################################################################

if __name__ == "__main__":
    script_dir = os.path.abspath('.\preprocessing')
    sys.path.append(script_dir)
    print(sys.path)


    path = 'src\data'
    txt_files,csv_files,pdf_files  = lister.find_files(path)
    print("files separated")
    embeddings = "hf"
    print(f"\n embedding :{embeddings} ")
    
    vector_db_pdf = load_db_chunk_persist_pdf(pdf_files,embeddings)
    vector_db_txt = load_db_chunk_persist_txt(txt_files,embeddings)
    vector_db_csv = load_db_persist_csv(csv_files,embeddings)
    
    
    
    
