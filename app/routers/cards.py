from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.config.database import get_db
from app.models.database import Card
from app.models.schemas import CardCreate, CardUpdate, CardResponse

router = APIRouter(prefix="/cards", tags=["cards"])


@router.post("/", response_model=CardResponse, status_code=status.HTTP_201_CREATED, response_model_by_alias=True)
def create_card(card: CardCreate, db: Session = Depends(get_db)):
    """Create a new card."""
    card_data = card.model_dump()
    if "metadata" in card_data:
        card_data["meta_data"] = card_data.pop("metadata")
    db_card = Card(**card_data)
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card


@router.get("/", response_model=List[CardResponse], response_model_by_alias=True)
def list_cards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """List all cards with pagination."""
    cards = db.query(Card).offset(skip).limit(limit).all()
    return cards


@router.get("/{card_id}", response_model=CardResponse, response_model_by_alias=True)
def get_card(card_id: int, db: Session = Depends(get_db)):
    """Get a specific card by ID."""
    card = db.query(Card).filter(Card.id == card_id).first()
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    return card


@router.put("/{card_id}", response_model=CardResponse, response_model_by_alias=True)
def update_card(card_id: int, card_update: CardUpdate, db: Session = Depends(get_db)):
    """Update a card."""
    db_card = db.query(Card).filter(Card.id == card_id).first()
    if not db_card:
        raise HTTPException(status_code=404, detail="Card not found")
    
    update_data = card_update.model_dump(exclude_unset=True)
    if "metadata" in update_data:
        update_data["meta_data"] = update_data.pop("metadata")
    
    for key, value in update_data.items():
        setattr(db_card, key, value)
    
    db.commit()
    db.refresh(db_card)
    return db_card


@router.delete("/{card_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_card(card_id: int, db: Session = Depends(get_db)):
    """Delete a card."""
    db_card = db.query(Card).filter(Card.id == card_id).first()
    if not db_card:
        raise HTTPException(status_code=404, detail="Card not found")
    
    db.delete(db_card)
    db.commit()
    return None
