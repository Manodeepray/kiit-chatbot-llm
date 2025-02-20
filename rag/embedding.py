from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

def hugging_face_embedding():
    print("start loading embeddings_hf")
    model_name = "sentence-transformers/all-mpnet-base-v2"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': False}
    hf = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    print("embeddings_hf loaded")
    return hf


def gemini_embeddings():
    print("start loading embeddings_gemini")

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    return embeddings
 
 
 
 
##################################################################################
 
if __name__=="__main__":
    # try:
    #     embeddings = hugging_face_embedding()
    #     # embeddings = gemini_embeddings()
    #     print(embeddings)
    # except Exception as e:
    #     print(f"error : {e}")
    
    
    model_name = "sentence-transformers/all-mpnet-base-v2"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': False}
    hf = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )