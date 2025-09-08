from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3
)

chat_history = [
    SystemMessage(content='you are helpful assistant'),
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        break
    result = model.invoke(chat_history)
    print("AI: ", result.content)
    chat_history.append(AIMessage(content=result.content))
print(chat_history)
