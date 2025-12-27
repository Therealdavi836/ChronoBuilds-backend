from fastapi import APIRouter
from services.external_api import fetch_characters_from_api
from urllib.parse import unquote

router = APIRouter()

@router.get("/{character_name}")
def get_build(character_name: str):
    character_name = unquote(character_name)  # Decodifica caracteres URL
    characters = fetch_characters_from_api()
    character = next((c for c in characters if c["name"].lower() == character_name.lower()), None)
    
    if not character:
        return {"error": "Character not found"}

    build = {
        "character": character["name"],
        "weapon": "Weapon recomendado basado en su rol",
        "artifacts": ["Artifact 1", "Artifact 2", "Artifact 3", "Artifact 4"],
        "stats": {
            "ATK%": "30%",
            "CRIT Rate": "15%",
            "CRIT DMG": "50%"
        },
        "notes": "Esta build maximiza el DPS del personaje."
    }

    return {"build": build}