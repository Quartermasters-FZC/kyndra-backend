from fastapi import APIRouter
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
import os

router = APIRouter()

# Load OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class PromptRequest(BaseModel):
    question: str

@router.post("/ask-ai")
async def ask_ai(request: PromptRequest):
    try:
        chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.5, model="gpt-4")
        response = chat([HumanMessage(content=request.question)])
        return {"response": response.content}
    except Exception as e:
        return {"error": str(e)}
