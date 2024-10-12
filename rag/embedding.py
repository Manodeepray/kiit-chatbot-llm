from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def hugging_face_embeddding():
    model_name = "sentence-transformers/all-mpnet-base-v2"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': False}
    hf = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    print("hf embedding loaded")
    return hf

def gemini_embeddings():
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    return embeddings
    

def sentence_transformer_embedding():
     embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
     print(" sentence_transformer_embedding loaded")

     return embedding_function
 
 
 
##################################################################################
 
if __name__=="__main__":
    embeddings = gemini_embeddings()