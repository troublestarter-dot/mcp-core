from fastapi import APIRouter, Depends, HTTPException, UploadFile, File as FastAPIFile, status
from sqlalchemy.orm import Session
from typing import List
import os
import shutil
from pathlib import Path
from app.config.database import get_db
from app.config.settings import settings
from app.models.database import File
from app.models.schemas import FileResponse

router = APIRouter(prefix="/files", tags=["files"])

# Ensure upload directory exists
UPLOAD_DIR = Path(settings.file_storage_path)
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/upload", response_model=FileResponse, status_code=status.HTTP_201_CREATED)
async def upload_file(file: UploadFile = FastAPIFile(...), db: Session = Depends(get_db)):
    """Upload a file to the server."""
    try:
        # Generate unique filename
        file_path = UPLOAD_DIR / file.filename
        counter = 1
        original_name = file.filename
        while file_path.exists():
            name_parts = original_name.rsplit(".", 1)
            if len(name_parts) == 2:
                file_path = UPLOAD_DIR / f"{name_parts[0]}_{counter}.{name_parts[1]}"
            else:
                file_path = UPLOAD_DIR / f"{original_name}_{counter}"
            counter += 1
        
        # Save file to disk
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Get file size
        file_size = file_path.stat().st_size
        
        # Create database record
        db_file = File(
            filename=file.filename,
            filepath=str(file_path),
            file_type=file.content_type,
            file_size=file_size
        )
        db.add(db_file)
        db.commit()
        db.refresh(db_file)
        
        return db_file
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading file: {str(e)}")


@router.get("/", response_model=List[FileResponse])
def list_files(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """List all files with pagination."""
    files = db.query(File).offset(skip).limit(limit).all()
    return files


@router.get("/{file_id}", response_model=FileResponse)
def get_file(file_id: int, db: Session = Depends(get_db)):
    """Get file metadata by ID."""
    file = db.query(File).filter(File.id == file_id).first()
    if not file:
        raise HTTPException(status_code=404, detail="File not found")
    return file


@router.delete("/{file_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_file(file_id: int, db: Session = Depends(get_db)):
    """Delete a file."""
    db_file = db.query(File).filter(File.id == file_id).first()
    if not db_file:
        raise HTTPException(status_code=404, detail="File not found")
    
    # Delete file from disk if it exists
    file_path = Path(db_file.filepath)
    if file_path.exists():
        file_path.unlink()
    
    # Delete database record
    db.delete(db_file)
    db.commit()
    return None
