

from langchain.vectorstores import FAISS
import embedding

def rank_across_vector_stores(query, vectorstores):
  results = []
  scores = []
  docs = []
  for vectorstore in vectorstores:
    vector_store_results = vectorstore.similarity_search_with_score(query, k = 1)  # Replace with appropriate method
    results.extend(vector_store_results)
    #print(vectorstore , vector_store_results )
    for doc, score in results:
        scores.append(score)
        docs.append(doc)
        print(f"* [SIM={score:3f}] {doc.page_content} [{doc.metadata}]")

  # Implement ranking logic here
  # For simplicity, let's sort by the combined similarity score
  #results.sort(key=lambda x: x.metadata['score'], reverse=True)

  return results , docs , scores


if __name__ == "__main__":
    query = input("enter query : ")

    embeddings = embedding.hugging_face_embeddding()
    vs_pdf = FAISS.load_local(folder_path="artifacts/pdf_vectorstore",embeddings = embeddings ,allow_dangerous_deserialization= True)
    vs_txt = FAISS.load_local(folder_path="artifacts/txt_vectorstore",embeddings = embeddings ,allow_dangerous_deserialization= True)
    vs_csv = FAISS.load_local(folder_path="artifacts/csv_vectorstore",embeddings = embeddings ,allow_dangerous_deserialization= True)
    
    vs_list = [vs_pdf , vs_txt , vs_csv]
    results , docs , scores = rank_across_vector_stores(query=query , vectorstores= vs_list)
    print("\n results :\n" , results)
    print("\n docs :\n" )
    for i in range(len(docs)):
        print(f"\n doc[ {i} ] :" , docs[i])
        
    print("\n sims :\n" , scores)