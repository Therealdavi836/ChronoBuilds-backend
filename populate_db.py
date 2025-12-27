from sqlalchemy.orm import Session
from database import SessionLocal, Base, engine
from models import Character, Build
from services.external_api import fetch_characters_from_api

# Crear las tablas si no existen
Base.metadata.create_all(bind=engine)

def populate_characters():
    db: Session = SessionLocal()
    try:
        characters = fetch_characters_from_api()
        for c in characters:
            # Evitar duplicados
            exists = db.query(Character).filter(Character.name == c["name"]).first()
            if not exists:
                new_char = Character(
                    name=c["name"],
                    element=c["element"],
                    role=c["role"],
                    weapon=c.get("weapon", "Unknown"),
                    rarity=c.get("rarity", 5)
                )
                db.add(new_char)
        db.commit()
        print(f"Se poblaron {len(characters)} personajes en la base de datos.")
    finally:
        db.close()

if __name__ == "__main__":
    populate_characters()