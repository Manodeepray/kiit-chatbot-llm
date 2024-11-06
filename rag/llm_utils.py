import requests
from langchain_community.llms.huggingface_hub import HuggingFaceHub
from artifacts import keys
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from langchain_ollama import OllamaLLM



HUGGINGFACEHUB_API_TOKEN = keys.HUGGINGFACEHUB_API_TOKEN
GOOGLE_API_KEY = keys.GOOGLE_API_KEY
def llm_api_request(query_text , HUGGINGFACEHUB_API_TOKEN):
    
	API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B"
	headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"}

	def query(payload):
		response = requests.post(API_URL, headers=headers, json=payload)
		return response.json()
		
	output = query({
		"inputs": "Can you please let us know more details about your ",
	})
 
	output = query({"inputs": query_text})
 
	return output



def load_llm_hf(HUGGINGFACEHUB_API_TOKEN):
    
    
    llms = ["meta-llama/Meta-Llama-3-8B","mistralai/Mistral-7B-v0.1","google/gemma-7b","google/gemma-2-27b"]
    
    
    hf = HuggingFaceHub(
    repo_id=llms[1],
    model_kwargs={"temperature": 0.1, "max_length": 500},
    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN
    )

    llm = hf
    print("llm loaded \n")
    return llm


def load_llm_gemini(GOOGLE_API_KEY):
	if "GOOGLE_API_KEY" not in os.environ:
		os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
	llm = ChatGoogleGenerativeAI(
		model="gemini-1.5-flash",
		temperature=0,
		max_tokens=None,
		timeout=None,
		max_retries=2,
	)
	print("llm loaded \n")

	return llm
    

def load_llm_ollama(llm_id):
    #  llm_id = llama3.2:3b
    llm = OllamaLLM(model= llm_id)
    
    return llm



if __name__ == "__main__":
    llm = load_llm_ollama("llama3.2:3b")
    response = llm.invoke("The first man on the moon was ...")
    print(response)


