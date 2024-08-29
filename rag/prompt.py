from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.prompts import ChatPromptTemplate

prompt_template = PromptTemplate(
    input_variables=["question", "context"],
    template="Based on the following context:\n{context}\nAnswer the question:\n{question}"
)



def context_q_prompt():
    contextualize_q_system_prompt = (
        "Given a chat history and the latest user question "
        "which might reference context in the chat history, "
        "formulate a standalone question which can be understood "
        "without the chat history. Do NOT answer the question, "
        "just reformulate it if needed and otherwise return it as is."
    )

    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", contextualize_q_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )
    return contextualize_q_prompt


def prompt_template_mempry():

    template = (
        "Combine the chat history and follow up question into "
        "a Follow up question if it requires."
        " otherwise answer the question as a standalone  question: {input}"
    )
    Prompt_template = PromptTemplate.from_template(template)
    return Prompt_template