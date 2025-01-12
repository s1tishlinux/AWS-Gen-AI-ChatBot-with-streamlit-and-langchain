from langchain_core.messages import HumanMessage, AIMessage
from langchain_aws import ChatBedrock

def demo_chatbot():
    demo_llm = ChatBedrock(
        credentials_profile_name='default',
        model_id='anthropic.claude-3-haiku-20240307-v1:0',
        model_kwargs={
            "max_tokens": 300,
            "temperature": 0.1,
            "top_p": 0.9,
            "stop_sequences": ["\n\nHuman:"]
        }
    )
    return demo_llm

def demo_memory():
    return []  # Return empty list for initial memory

def demo_conversation(input_text: str, memory: list) -> str:
    llm = demo_chatbot()
    
    # Add the new message to memory
    memory.append(HumanMessage(content=input_text))
    
    # Get response from the model
    response = llm.invoke(memory)
    
    # Add AI response to memory
    memory.append(AIMessage(content=response.content))
    
    return response.content
