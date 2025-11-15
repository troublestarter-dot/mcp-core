from fastapi import FastAPI
from .routes import router
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title=settings.APP_NAME, version="0.1.0")

# Настройка CORS (если требуется)
origins = settings.CORS_ORIGINS or ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")

@app.get("/healthz", tags=["health"])
async def healthz():
    return {"status": "ok", "service": settings.APP_NAME}
