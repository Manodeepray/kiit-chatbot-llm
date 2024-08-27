from langchain.chains.conversation.base import  ConversationChain
from langchain.memory.buffer import ConversationBufferMemory
from langchain.memory.token_buffer import ConversationTokenBufferMemory
from langchain.memory.buffer_window import ConversationBufferWindowMemory

def converstion_buffer_whole(llm):
    memory = ConversationBufferMemory( memory_key="chat_history" ,  return_messages=True)
    conversation = ConversationChain(
        llm=llm, 
        memory = memory,
        verbose=False
    )
    
    return conversation



def converstion_buffer_window(llm , chat_nums):  #chatnums = k =1
    memory = ConversationBufferWindowMemory(memory_key="chat_history",k=chat_nums)
    conversation = ConversationChain(
        llm=llm, 
        memory = memory,
        verbose=False
    )
    
    return conversation


def converstion_buffer_token(llm , tokens):  #chatnums = k =1
    memory = ConversationTokenBufferMemory( memory_key="chat_history" ,max_token_limit=tokens)

    conversation = ConversationChain(
        llm=llm, 
        memory = memory,
        verbose=False
    )
    
    return conversation
