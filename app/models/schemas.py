from pydantic import BaseModel, Field, ConfigDict
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


class CardResponse(BaseModel):
    id: int
    title: str
    content: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = Field(None, validation_alias="meta_data", serialization_alias="metadata")
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


# Event schemas
class EventBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    event_type: str = Field(..., min_length=1, max_length=100)
    metadata: Optional[Dict[str, Any]] = None


class EventCreate(EventBase):
    pass


class EventResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    event_type: str
    metadata: Optional[Dict[str, Any]] = Field(None, validation_alias="meta_data", serialization_alias="metadata")
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


# File schemas
class FileBase(BaseModel):
    filename: str
    file_type: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class FileResponse(BaseModel):
    id: int
    filename: str
    filepath: str
    file_type: Optional[str] = None
    file_size: Optional[int] = None
    metadata: Optional[Dict[str, Any]] = Field(None, validation_alias="meta_data", serialization_alias="metadata")
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
