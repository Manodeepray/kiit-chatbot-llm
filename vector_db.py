from rag  import lister 
from rag import merging
from preprocessing import chunking , combiner
from langchain.vectorstores import Chroma
import chromadb
from rag import embedding
import faiss
import numpy as np
import  os
import sys
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader

from langchain_community.document_loaders import CSVLoader


'''def load_db_chunk_persist_txt(txt_files , embeddings):
    
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
'''






















def combined_pdf_vectorstore(output_pdf):
    def pdf_loader(file_path):
            
        loader = PyPDFLoader(file_path)

        docs = loader.load()

        print(len(docs))
        #print(docs[0].page_content[0:100])
        #print(docs[0].metadata)

        return docs
    def splitting(docs):
        text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 700,
        chunk_overlap  = 50,
        )
        docs_after_split = text_splitter.split_documents(docs)

        #print(docs_after_split[0])
        
        return docs_after_split

    def load_vectorstore(docs_after_split,huggingface_embeddings):
        vectorstore = FAISS.from_documents(docs_after_split, huggingface_embeddings)
        print("vector store loaded \n")
        return vectorstore

    docs = pdf_loader(output_pdf)
    docs_after_split = splitting(docs)
    
    hf = embedding.hugging_face_embeddding()
    
    vectorstore = load_vectorstore(docs_after_split , hf)
    

    return vectorstore




def combined_txt_vectorstore(output_txt):
    def txt_loader(file_path):
            
        loader = TextLoader(file_path , encoding = "utf-8")

        docs = loader.load()

        print(len(docs))
        #print(docs[0].page_content[0:100])
        #print(docs[0].metadata)

        return docs
    def splitting(docs):
        text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 700,
        chunk_overlap  = 50,
        )
        docs_after_split = text_splitter.split_documents(docs)

        #print(docs_after_split[0])
        
        return docs_after_split

    def load_vectorstore(docs_after_split,huggingface_embeddings):
        vectorstore = FAISS.from_documents(docs_after_split, huggingface_embeddings)
        print("vector store loaded \n")
        return vectorstore

    docs = txt_loader(output_txt)
    docs_after_split = splitting(docs)
    
    hf = embedding.hugging_face_embeddding()
    
    vectorstore = load_vectorstore(docs_after_split , hf)
    

    return vectorstore


def combined_csv_vectorstore(output_csv):
    def csv_loader(file_path):
        
        loader = CSVLoader(file_path)
        docs = loader.load()
        
        
        
        print(len(docs))
        #print(docs[0].page_content[0:100])
        #print(docs[0].metadata)

        return docs
    
    def splitting(docs):
        text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap  = 50,
        )
        docs_after_split = text_splitter.split_documents(docs)

        #print(docs_after_split[0])
        
        return docs_after_split

    def load_vectorstore(docs_after_split,huggingface_embeddings):
        vectorstore = FAISS.from_documents(docs_after_split, huggingface_embeddings)
        print("vector store loaded \n")
        return vectorstore

    docs = csv_loader(output_csv)
    docs_after_split = splitting(docs)
    
    hf = embedding.hugging_face_embeddding()
    
    vectorstore = load_vectorstore(docs_after_split , hf)
    

    return vectorstore









def save_vectorstore(vectorstore , save_path):
    vectorstore.save_local(save_path)


    return

def load_vectorstore(load_path , embeddings):
    new_vector_store = FAISS.load_local(
    load_path, embeddings, allow_dangerous_deserialization=True
    )

    return new_vector_store




def load_and_save_Vector_stores():
    
    script_dir = os.path.abspath('.\preprocessing')
    sys.path.append(script_dir)
    print(sys.path)


    path = 'src\data'
    
    output_pdf = "src/combined_data/combined.pdf"
    output_txt = "src\combined_data\combined.txt"
    output_csv = "src/combined_data/combined.csv" 
    
    
    pdf_vectorstore_path = "artifacts/pdf_vectorstore"
    txt_vectorstore_path = "artifacts/txt_vectorstore"
    csv_vectorstore_path = "artifacts/csv_vectorstore"
    
    
    
    txt_files,csv_files,pdf_files  = lister.find_files(path)
    
    combiner_class = combiner.Combiner()
    
    
    
    
    
    
    combiner_class.pdf_combiner(pdf_files , output_pdf)
    
    combiner_class.txt_combiner(txt_files , output_txt)
    
    combiner_class.csv_cbmbiner(csv_files , output_csv)
    
    
    
    print("files combined")
    
    try:
        vectorstore_pdf = combined_pdf_vectorstore(output_pdf)
        print("pdf vectorstore created")
    except Exception as e:
        print(f"error in creating pdf vectorstore {e}")
        
    try:
        vectorstore_txt = combined_txt_vectorstore(output_txt)
        print("txt vectorstore created")
    except Exception as e:
        print(f"error in creating txt vectorstore {e}")
        
    try:
        vectorstore_csv = combined_csv_vectorstore(output_csv)
        print("csv vectorstore created")
    except Exception as e:
        print(f"error in creating txt vectorstore {e}")
        
        
    save_vectorstore(vectorstore = vectorstore_pdf , save_path = pdf_vectorstore_path)
    save_vectorstore(vectorstore = vectorstore_txt , save_path = txt_vectorstore_path)
    save_vectorstore(vectorstore = vectorstore_csv , save_path = csv_vectorstore_path)
    
    
    
    
    
    
    
    
    
    
    
    return vectorstore_pdf , vectorstore_txt , vectorstore_csv , pdf_vectorstore_path , txt_vectorstore_path, csv_vectorstore_path 
    
####################################################################################################################

if __name__ == "__main__":
   
    
    
    vectorstore_pdf , vectorstore_txt , vectorstore_csv , pdf_vectorstore_path , txt_vectorstore_path, csv_vectorstore_path =load_and_save_Vector_stores()


    
    '''combined_db = merging.merging_db_FAISS(pdf_db = vectorstore_pdf,
                             txt_db = vectorstore_txt ,
                             csv_db = vectorstore_txt)
    
    save_vectorstore(combined_db , save_path = "./artifacts/combined_vectorstore")
    '''
    
    '''query = "tell me about dean suprava patnaik"
    
    vector_stores  = [vectorstore_pdf, vectorstore_csv , vectorstore_txt]
    results = ranking.rank_across_vector_stores( query = query , vectorstores = vector_stores)
    
    print(results)
    
    
    '''
    
    
    
    '''embeddings = "hf"
    print(f"\n embedding :{embeddings} ")
    
    
    
    vector_db_pdf = load_db_chunk_persist_pdf(pdf_files,embeddings)
    vector_db_txt = load_db_chunk_persist_txt(txt_files,embeddings)
    vector_db_csv = load_db_persist_csv(csv_files,embeddings)'''
    
    
    
    
