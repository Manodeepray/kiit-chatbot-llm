from langchain_community.document_loaders import JSONLoader
from langchain_community.vectorstores import Chroma
from langchain_community.vectorstores import FAISS
from embedding import *

def return_db_chroma(filepath):
    
    embedding_function =sebtence_transformer_embedding()

    hf = hugging_face_embeddding()

    loader = JSONLoader(file_path=filepath, jq_schema=  "data", text_content=False)
    documents = loader.load()

    db1 = Chroma.from_documents(documents, embedding_function)
    db2 = Chroma.from_documents(documents, hf)

    
    
    return db1 , db2

def return_db_faiss(filepath):
    
    embedding_function =sebtence_transformer_embedding()

    hf = hugging_face_embeddding()

    loader = JSONLoader(file_path=filepath, text_content=False)
    documents = loader.load()

    db1 = FAISS.from_documents(documents, embedding_function)
    db2 = FAISS.from_documents(documents, hf)

    
    
    return db1 , db2







    
    






if __name__ =="__main__":
    
    json_path = "src\json\output.json"
    db1  , db2 = return_db_chroma(json_path)
    
    #query = "What year did albert einstein win the nobel prize?"
    query = str(input("enter ur query : "))
    docs1 = db1.similarity_search(query)
    
    print(docs1[0].page_content)

    docs2 = db2.similarity_search(query)
    
    print(docs2[0].page_content)
