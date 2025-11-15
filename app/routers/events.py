from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.config.database import get_db
from app.models.database import Event
from app.models.schemas import EventCreate, EventResponse

router = APIRouter(prefix="/events", tags=["events"])


@router.post("/", response_model=EventResponse, status_code=status.HTTP_201_CREATED, response_model_by_alias=True)
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    """Create a new event."""
    event_data = event.model_dump()
    if "metadata" in event_data:
        event_data["meta_data"] = event_data.pop("metadata")
    db_event = Event(**event_data)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


@router.get("/", response_model=List[EventResponse], response_model_by_alias=True)
def list_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """List all events with pagination."""
    events = db.query(Event).offset(skip).limit(limit).all()
    return events


@router.get("/{event_id}", response_model=EventResponse, response_model_by_alias=True)
def get_event(event_id: int, db: Session = Depends(get_db)):
    """Get a specific event by ID."""
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@router.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_event(event_id: int, db: Session = Depends(get_db)):
    """Delete an event."""
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    db.delete(db_event)
    db.commit()
    return None
