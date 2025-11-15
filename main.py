from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import settings
from app.config.database import Base, engine
from app.routers import cards, events, files

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="MCP Core API",
    description="Универсальное ядро MCP — автономный сервер FastAPI для управления карточками, событиями и файлами платформы Родная GPT",
    version="1.0.0"
)

# Configure CORS
origins = settings.allowed_origins.split(",") if settings.allowed_origins != "*" else ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(cards.router)
app.include_router(events.router)
app.include_router(files.router)


@app.get("/")
async def root():
    """Root endpoint - API health check."""
    return {
        "message": "MCP Core API is running",
        "version": "1.0.0",
        "endpoints": {
            "cards": "/cards",
            "events": "/events",
            "files": "/files",
            "docs": "/docs",
            "openapi": "/openapi.json"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
