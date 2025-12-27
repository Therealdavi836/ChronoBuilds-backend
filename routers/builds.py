from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.character import Character
from models.build import Build
from services.build_logic import generate_build
from urllib.parse import unquote
import json

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{character_name}")
def get_character_build(character_name: str, db: Session = Depends(get_db)):
    name = unquote(character_name)
    character = db.query(Character).filter(Character.name.ilike(name)).first()

    if not character:
        raise HTTPException(status_code=404, detail="Character not found")

    try:
        build = generate_build(character, db)
        
        # Clean the data for Next.js
        return {
            "build": {
                "character": character.name,
                "weapon": build.weapon,
                "artifacts": json.loads(build.artifacts) if isinstance(build.artifacts, str) else build.artifacts,
                "stats": json.loads(build.stats) if isinstance(build.stats, str) else build.stats,
                "notes": build.notes
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))