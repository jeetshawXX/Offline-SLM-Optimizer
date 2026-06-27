from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="Offline SLM Optimizer",
    description="Backend API for Offline Small Language Model Optimization",
    version="1.0.0"
)

app.include_router(router)