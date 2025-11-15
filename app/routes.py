from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["root"])
async def root():
    return {"message": "MCP Core FastAPI server"}
