
from langchain.retrievers import EnsembleRetriever

from langchain.vectorstores import Chroma



def merging_db_chroma(pdf_docs , txt_docs , csv_docs,embeddings):
    chroma_directory = ""
    
    db = Chroma(persist_directory=chroma_directory, embedding_function=embeddings)

    db.add_documents(documents=pdf_docs)
    db.add_documents(documents=txt_docs)  
    db.add_documents(documents=csv_docs)  
    return db

def merging_db_FAISS(pdf_db , txt_db , csv_db):
    #FAISS VECTOR DB's
    pdf_db.merge_from(txt_db)
    pdf_db.merge_from(csv_db)
    combined_db = pdf_db
    
    return combined_db


def ensemble_retriever(pdf_retriever , csv_retriever , txt_retriever):
    ensemble_retriever = EnsembleRetriever([pdf_retriever , csv_retriever , txt_retriever] , weights=[0.33 , 0.33 , 0.33])
    return  ensemble_retriever