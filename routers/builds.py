from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.build_logic import generate_build
from models.character import Character
from models.build import Build  # Corrected Import
from database import SessionLocal
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
def get_build(character_name: str, db: Session = Depends(get_db)):
    character_name = unquote(character_name)
    # ilike is great here for case-insensitive matching
    character = db.query(Character).filter(Character.name.ilike(character_name)).first()

    if not character:
        return {"error": "Character not found"}

    build = generate_build(character, db)

    build_data = {
        "character": character.name,
        "weapon": build.weapon,
        "artifacts": json.loads(build.artifacts) if isinstance(build.artifacts, str) else build.artifacts,
        "stats": json.loads(build.stats) if isinstance(build.stats, str) else build.stats,
        "notes": build.notes
    }

    return {"build": build_data}