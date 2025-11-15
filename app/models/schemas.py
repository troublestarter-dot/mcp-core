from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime


# Card schemas
class CardBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    content: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class CardCreate(CardBase):
    pass


class CardUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    content: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class CardResponse(CardBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


# Event schemas
class EventBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    event_type: str = Field(..., min_length=1, max_length=100)
    metadata: Optional[Dict[str, Any]] = None


class EventCreate(EventBase):
    pass


class EventResponse(EventBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True


# File schemas
class FileBase(BaseModel):
    filename: str
    file_type: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class FileResponse(FileBase):
    id: int
    filepath: str
    file_size: Optional[int] = None
    created_at: datetime
    
    class Config:
        from_attributes = True
