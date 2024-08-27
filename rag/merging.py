
from langchain.retrievers.ensemble import EnsembleRetriever


def merging_db_FAISS(pdf_db , txt_db , csv_db):
    #FAISS VECTOR DB's
    pdf_db.merge_from(txt_db)
    pdf_db.merge_from(csv_db)
    combined_db = pdf_db
    
    return combined_db


def ensemble_retriever(pdf_retriever , csv_retriever , txt_retriever):
    ensemble_retriever = EnsembleRetriever([pdf_retriever , csv_retriever , txt_retriever] , weights=[0.33 , 0.33 , 0.33])
    return  ensemble_retriever
