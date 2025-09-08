from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3
)

messages=[
    SystemMessage(content='you are helpful assistant'),
    HumanMessage(content='tell me about pandas')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))
print(messages)