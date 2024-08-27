import requests
from langchain_community.llms.huggingface_hub import HuggingFaceHub
from artifacts import keys


HUGGINGFACEHUB_API_TOKEN = keys.HUGGINGFACEHUB_API_TOKEN

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



def load_llm(HUGGINGFACEHUB_API_TOKEN):
    
    
    llms = ["meta-llama/Meta-Llama-3-8B","mistralai/Mistral-7B-v0.1","google/gemma-7b"]
    
    
    hf = HuggingFaceHub(
    repo_id=llms[1],
    model_kwargs={"temperature": 0.1, "max_length": 500},
    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN
    )

    llm = hf
    print("llm loaded \n")
    return llm



