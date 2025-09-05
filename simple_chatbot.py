from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3
)

chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append({"role": "user", "content": user_input})
    if user_input.lower() == "exit":
        break
    result = model.invoke(chat_history)
    print("AI: ", result.content)
    chat_history.append({"role": "assistant", "content": result.content})
print(chat_history)
