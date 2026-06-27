from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from engine.inference_engine import InferenceEngine
from models.chat_models import ChatRequest, ChatResponse

router = APIRouter()

engine = InferenceEngine()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    answer = engine.process(request.prompt)

    return ChatResponse(response=answer)


@router.post("/chat/stream")
def stream_chat(request: ChatRequest):

    return StreamingResponse(
        engine.process_stream(request.prompt),
        media_type="text/plain"
    )