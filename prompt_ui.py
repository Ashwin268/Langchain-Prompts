from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from huggingface_hub import InferenceClient
import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()
token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
print("Token loaded:", token[:10], "...")  # sanity check
load_dotenv()
token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="conversational",
    huggingfacehub_api_token=token
)

model = ChatHuggingFace(llm=llm)
response = model.invoke("Who is the inventor of 0?")
print(response)