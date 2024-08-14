import os
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv('/home/rushikesh/Downloads/Udemy/GenAI/open_ai/Final End to End Applications/LCEL/.env')

#Initializing the llm model
model = Ollama(model="llama2:latest")

#Creating Prompt Template
system_template = "Translate the following into {language}"
prompt_template = ChatPromptTemplate.from_messages(
    [
        ('system',system_template),
        ("user","{text}")
        
        
    ]
)

#Output Parser
parser=StrOutputParser()


#create chain

def server_chain():
    chain=prompt_template|model|parser
    return chain




