from fastapi import APIRouter

from models.chat_models import ChatRequest, ChatResponse
from engine.inference_engine import InferenceEngine

router = APIRouter()

engine = InferenceEngine()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    answer = engine.process(request.prompt)

    return ChatResponse(response=answer)