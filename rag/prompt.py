from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate(
    input_variables=["question", "context"],
    template="Based on the following context:\n{context}\nAnswer the question:\n{question}"
)

def prompt_template_mempry():

    template = (
        "Combine the chat history and follow up question into "
        "a standalone question. Chat History: {chat_history}"
        "Follow up question: {question}"
    )
    Prompt_template = PromptTemplate.from_template(template)
    return Prompt_template