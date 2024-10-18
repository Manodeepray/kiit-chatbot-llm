#from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
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
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    return embeddings
    
'''
def sentence_transformer_embedding():
     embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
     print(" sentence_transformer_embedding loaded")

     return embedding_function'''
 
 
 
##################################################################################
 
if __name__=="__main__":
    try:
        embeddings = hugging_face_embedding()
        print(embeddings)
    except Exception as e:
        print(f"error : {e}")