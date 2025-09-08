from langchain_core.prompts import ChatPromptTemplate

chatTemplate = ChatPromptTemplate([
    ('system','you are an helpful {domain} expert'),
    ('human','Tell me about this person, Who is {topic}')    
])
prompt = chatTemplate.invoke({'domain':'cricket','topic':'MS DHONI'})

print(prompt)