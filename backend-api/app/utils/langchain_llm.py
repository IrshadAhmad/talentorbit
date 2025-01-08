from langchain_openai import OpenAI, ChatOpenAI
from app.core.config import settings


def invoke(chats):
    llm = ChatOpenAI(api_key=settings.OPENAI_API_KEY, model="gpt-4o-mini")
    try:
        result = llm.invoke(chats).content 
        return result
    except Exception as e:
        return {"error": "Exception", "message": str(e)}