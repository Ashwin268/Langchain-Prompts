from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Define the template correctly
chatTemplate = ChatPromptTemplate.from_messages([
    ('system', 'you are a helpful assistant'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

# Load chat history from file
chat_history = []
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print("Loaded chat history:", chat_history)

# Create prompt (fill in variables)
prompt = chatTemplate.format_messages(
    chat_history=chat_history,
    query='Where is my refund'
)

print(prompt)
