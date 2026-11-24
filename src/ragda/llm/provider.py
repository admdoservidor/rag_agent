from langchain_groq import ChatGroq

from ragda.core.config import api_key

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=api_key,
    temperature=0,
    max_retries=2,
)