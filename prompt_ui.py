import streamlit as st
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")


llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3,
    max_output_tokens=100
)

st.title("Gemini LangChain Demo")

prompt = st.text_input("Trying Gemini Prompt")

if prompt:
    response = llm.invoke(prompt)
    st.write("### Gemini says:")
    st.write(response.content)
