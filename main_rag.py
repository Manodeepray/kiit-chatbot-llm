from rag import llm_utils, memory , retriever , prompt , merging , embedding
import faiss
from langchain_community.vectorstores import FAISS
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from artifacts import keys
import google.generativeai as genai

def chatbot_rag(mode):
    #mode = 'GEMINI' 
    # mode = 'HF'
    HUGGINGFACEHUB_API_TOKEN = keys.HUGGINGFACEHUB_API_TOKEN
    GOOGLE_API_KEY = keys.GOOGLE_API_KEY
    LLM_ID = "deepseek-r1:1.5b"
    
    
    
    try:
        if mode == 'GEMINI':
            embeddings_g = embedding.gemini_embeddings()
        elif mode == 'HF':
            embeddings_hf = embedding.hugging_face_embedding()
        elif mode == 'OLLAMA':
            embeddings_hf = embedding.hugging_face_embedding()
        print("embedding loaded")
    except Exception as e:
        print(f"error loading the embeddings : {e}")


    try:
        if mode == 'GEMINI':
            llm_model = llm_utils.load_llm_gemini(GOOGLE_API_KEY=GOOGLE_API_KEY)
        elif mode == 'HF':
            llm_model = llm_utils.load_llm_hf(HUGGINGFACEHUB_API_TOKEN = HUGGINGFACEHUB_API_TOKEN)
        elif mode == "OLLAMA":
            
            llm_model = llm_utils.load_llm_ollama(LLM_ID)
        print("llm loaded")
    except Exception as e:
        print(f"error loading model : {e}")
        
    #hugging face vectorstores
    if mode == 'HF':
        try:
            try:
                pdf_vectorstore = FAISS.load_local(folder_path="artifacts/pdf_vectorstore",embeddings = embeddings_hf ,allow_dangerous_deserialization= True)
                print("pdf vectorstore loaded")
            except Exception as e:
                print(f"error loading pdf vectorstore :{e}")
            
            try:    
                txt_vectorstore = FAISS.load_local(folder_path="artifacts/txt_vectorstore",embeddings = embeddings_hf ,allow_dangerous_deserialization= True)
                print("txt vectorstore loaded")
            except Exception as e:
                print(f"error loading txt vectorstore :{e}")
            
            try:    
                csv_vectorstore = FAISS.load_local(folder_path="artifacts/csv_vectorstore",embeddings = embeddings_hf ,allow_dangerous_deserialization= True)
                print("csv vectorstore loaded")
            except Exception as e:
                print(f"error loading csv vectorstore :{e}")
            
            
            
            print("all vectorstores loaded successfully")
        except Exception as e:
            
            print(f"error loading the vectorstores : {e}")
    elif mode == 'OLLAMA':
        try:
            try:
                pdf_vectorstore = FAISS.load_local(folder_path="artifacts/pdf_vectorstore",embeddings = embeddings_hf ,allow_dangerous_deserialization= True)
                print("pdf vectorstore loaded")
            except Exception as e:
                print(f"error loading pdf vectorstore :{e}")
            
            try:    
                txt_vectorstore = FAISS.load_local(folder_path="artifacts/txt_vectorstore",embeddings = embeddings_hf ,allow_dangerous_deserialization= True)
                print("txt vectorstore loaded")
            except Exception as e:
                print(f"error loading txt vectorstore :{e}")
            
            try:    
                csv_vectorstore = FAISS.load_local(folder_path="artifacts/csv_vectorstore",embeddings = embeddings_hf ,allow_dangerous_deserialization= True)
                print("csv vectorstore loaded")
            except Exception as e:
                print(f"error loading csv vectorstore :{e}")
            
            
            
            print("all vectorstores loaded successfully")
        except Exception as e:
            
            print(f"error loading the vectorstores : {e}")
            
            
    elif mode == 'GEMINI':
    # gemini vectorstore
        try:
            try:
                pdf_vectorstore = FAISS.load_local(folder_path="artifacts/pdf_vectorstore_gemini",embeddings = embeddings_g ,allow_dangerous_deserialization= True)
                print("pdf vectorstore loaded")
            except Exception as e:
                print(f"error loading pdf vectorstore :{e}")
            
            try:    
                txt_vectorstore = FAISS.load_local(folder_path="artifacts/txt_vectorstore_gemini",embeddings = embeddings_g ,allow_dangerous_deserialization= True)
                print("txt vectorstore loaded")
            except Exception as e:
                print(f"error loading txt vectorstore :{e}")
            
            try:    
                csv_vectorstore = FAISS.load_local(folder_path="artifacts/csv_vectorstore_gemini",embeddings = embeddings_g ,allow_dangerous_deserialization= True)
                print("csv vectorstore loaded")
            except Exception as e:
                print(f"error loading csv vectorstore :{e}")
            
            
            
            print("all vectorstores loaded successfully")
        except Exception as e:
            
            print(f"error loading the vectorstores : {e}")
        
        
        
        
        
    # creating retriever instances 
    
    
    
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
        
    # merging the 3 retrievers
        
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



def hf_response(chat_retriever_chain,query):
    chat_retriever_chain = chatbot_rag()
    query = query.lower()
    response = chat_retriever_chain.invoke({"input": query})
    
    return response

def llm_answer(query , context):
    llm_model = llm_utils.load_llm_hf(HUGGINGFACEHUB_API_TOKEN=keys.HUGGINGFACEHUB_API_TOKEN)
    prompt = f'''"You are an intelligent assistant capable of answering complex questions using a combination of document retrieval and reasoning. The context provided contains important information extracted from documents, and your task is to use this context to generate a clear, accurate response to the user query.

Context: {context}

User Query: {query}

Based on the context, provide the most relevant and detailed answer to the user query. If the context doesn't have enough information, suggest the next steps or additional information that might be useful."'''
    
    print(prompt)
    
    response = llm_model.invoke(prompt)
    return response


def gemini_response(chat_retriever_chain,query):
    query = query.lower()
    response = chat_retriever_chain.invoke({"input": query})
    print('response :',response)
    documents = response
    response = {}
    answer = []
    for document in documents:
        content = document.page_content.replace('\n', ' ')
        content = content.replace('\t',' ')
        answer.append(content)
    answer = answer[:5]
        
        
    template=f"Based on the following context:\n{answer}\nAnswer the question:\n{query}"
    #print(f"answer : \n {answer}\n answer_len :{len(answer)}")
    #llm_response  = llm_answer(query=query , context= answer)
    print("template : ",template)
    genai.configure(api_key = "AIzaSyBKsyvw-c3WFy9tWncfiWIPTC1-e_5XPiQ")

    model = genai.GenerativeModel("gemini-1.5-flash")
    llm_response = model.generate_content(template)
        
    print("llm_response",llm_response.text)
    
    
    return llm_response


def ollama_response(chat_retriever_chain,query):
    
    #setting the llm 
    llm_id = "deepseek-r1:1.5b"
    
    
    
    
    query = query.lower()
    response = chat_retriever_chain.invoke({"input": query})
    print('response :',response)
    documents = response
    response = {}
    answer = []
    for document in documents:
        content = document.page_content.replace('\n', ' ')
        content = content.replace('\t',' ')
        answer.append(content)
    context = answer[:5]
        
        
    template=f'''you are a chat bot helping students and parents for getting information about the college Based on the context and question given below.
    try to complete each answer and be friendly as if you are a student guide.
    keep the answers brief unless told to give large answers 
    documents = response
    
    context:\n  {context} \n               
    
    question:\n{query}'''
    #print(f"answer : \n {answer}\n answer_len :{len(answer)}")
    #llm_response  = llm_answer(query=query , context= answer)
    print("template : ",template)
    
    #loadind llama model
    
    llm = llm_utils.load_llm_ollama(llm_id=llm_id)

    llm_response = llm.invoke(template)
    
    print("\n \n llm_response :",llm_response)
    
    
    return llm_response

if __name__ == "__main__":
    

    # query = "What is Document testimonial about?"
      
    
    
    
    chat_retriever_chain = chatbot_rag()
    query = "empty"
    
    while(query!="exit"):
        query = input("enter your query :")
        query = query.lower()
        #response = gemini_response(chat_retriever_chain , query)
        response = ollama_response(chat_retriever_chain , query)
        
        
        
        
    