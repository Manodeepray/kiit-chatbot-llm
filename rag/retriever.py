
from rag.vector_db_json import *

#vector_store retriever

def vector_store_retirever(vectorstore):
    retriever = vectorstore.as_retriever()
    return retriever

s
if __name__ == "__main__":
    
    query = str(input("enter ur query : "))

    json_path = "src\json\output.json"
    db1 , db2 =  return_db_chroma(json_path)
    retriever1 = vector_store_retirever(db1)
    
    docs1 = retriever1.invoke(query)

    retriever2 = vector_store_retirever(db2)

    docs2 = retriever2.invoke(query)
    
    
    
    print("docs1 :", docs1 )
    
    print("docs2 :", docs2 )
    
    
    """retriever = db.as_retriever(
    search_type="similarity_score_threshold", search_kwargs={"score_threshold": 0.5}
    )"""

    '''retriever = db.as_retriever(search_type="mmr")

    '''