from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

#lANGSMITH TRACKING
os.environ["LANGCHAIN_API_KEY"] = "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"
os.environ["LANGCHAIN_TRACING_V2"] = "true"


#prompt Template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that can answer questions with humor."),
        ("user", "Question:{question}"),
    ]
)

#streamlit framework
st.title("Ask me anything Akshay")

question = st.text_input("Enter a question")



#llm
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
output_parser = StrOutputParser()
chain = prompt_template | llm | output_parser

#run the chain
result = chain.invoke({"question": question})
if question:
    st.write(result)
