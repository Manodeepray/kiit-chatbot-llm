from rag import memory , retriever , prompt , llm , merging , embedding
import faiss
from langchain_community.vectorstores import FAISS
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from artifacts import keys

def chatbot_rag():
    HUGGINGFACEHUB_API_TOKEN = keys.HUGGINGFACEHUB_API_TOKEN
    try:
        embeddings = embedding.hugging_face_embeddding()
        print("embedding loaded")
    except Exception as e:
        print(f"error loading the embeddings : {e}")


    try:
        llm_model = llm.load_llm(HUGGINGFACEHUB_API_TOKEN = HUGGINGFACEHUB_API_TOKEN)
        print("llm loaded")
    except Exception as e:
        print(f"error loading model : {e}")
        

    try:
        try:
            pdf_vectorstore = FAISS.load_local(folder_path="artifacts/pdf_vectorstore",embeddings = embeddings ,allow_dangerous_deserialization= True)
            print("pdf vectorstore loaded")
        except Exception as e:
            print(f"error loading pdf vectorstore :{e}")
        
        try:    
            txt_vectorstore = FAISS.load_local(folder_path="artifacts/txt_vectorstore",embeddings = embeddings ,allow_dangerous_deserialization= True)
            print("txt vectorstore loaded")
        except Exception as e:
            print(f"error loading txt vectorstore :{e}")
        
        try:    
            csv_vectorstore = FAISS.load_local(folder_path="artifacts/csv_vectorstore",embeddings = embeddings ,allow_dangerous_deserialization= True)
            print("csv vectorstore loaded")
        except Exception as e:
            print(f"error loading csv vectorstore :{e}")
        
        
        
        print("all vectorstores loaded successfully")
    except Exception as e:
        
        print(f"error loading the vectorstores : {e}")
    
    
    
    
    try:
        try:
            txt_retriever = retriever.vector_store_retirever(txt_vectorstore)

            print("txt retriever loaded")
        except Exception as e:
            print(f"error loading txt retriever :{e}")
        
        try:    
            pdf_retriever = retriever.vector_store_retirever(pdf_vectorstore)

            print("pdf retriever loaded")
        except Exception as e:
            print(f"error loading pdf retriever :{e}")
        
        try:    
            csv_retriever = retriever.vector_store_retirever(csv_vectorstore)
    
            print("csv retriever loaded")
        except Exception as e:
            print(f"error loading csv retriever :{e}")
        
        
        
        print("all retriever loaded successfully")
    except Exception as e:
        
        print(f"error loading the retrievers : {e}")
        
        
        
    try:
        ensemble_retriever = merging.ensemble_retriever(pdf_retriever=pdf_retriever ,
                            txt_retriever=txt_retriever ,
                            csv_retriever=csv_retriever)
        print("ensemble retriever loaded successfully")
    except Exception as e:
        print(f"error loading the ensemble retriever : {e}")

        
    '''try:
        rag_memory = memory.ConversationBufferMemory(memory_key='chat_history' , return_messages= True)
        print("rag memory func loaded successfully")
    except Exception as e:
        print(f"error loading rag memory func : {e}")'''
        
    try:
        prompt_template = prompt.context_q_prompt()
        print("prompt_template loaded successfully")
    except Exception as e:
        print(f"error loading prompt_template : {e}")
        
        
        
#    ConversationalRetrievalChain is depreceated 
    '''try:
        conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm_model,
        retriever=ensemble_retriever,
        memory=rag_memory,
        prompt=prompt_template
    )
        print("conversation_chain loaded successfully")
    except Exception as e:
        print(f"error loading conversation_chain : {e}")'''
        
        
        
        
        
        
    try:
        chat_retriever_chain = create_history_aware_retriever(
        llm = llm_model, retriever=ensemble_retriever, prompt=prompt_template
        )
        
        print("chat_retriever_chain loaded successfully")
    except Exception as e:
        print(f"error loading chat_retriever_chain : {e}")
            
    """response = chat_retriever_chain.invoke({"input": query})
"""
    '''try:
        print("generating response\n")
        print(f"response generated successfully \n response : {response}")

    except Exception as e:
        print(f"error generating response : {e}")'''

       
    


    return chat_retriever_chain


if __name__ == "__main__":
#    query = "What is Document testimonial about?"
    chat_retriever_chain = chatbot_rag()
    query = "empty"
    while(query!="exit"):
        query = input("enter your query :")
        query = query.lower()
        response = chat_retriever_chain.invoke({"input": query})

        print(response)
        