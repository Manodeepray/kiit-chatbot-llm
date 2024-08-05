from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings


def hugging_face_embeddding():
    model_name = "sentence-transformers/all-mpnet-base-v2"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': False}
    hf = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    
    return hf


def sebtence_transformer_embedding():
     embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
     return embedding_function