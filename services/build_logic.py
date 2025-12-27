from sqlalchemy.orm import Session
from models.character import Character
from models.build import Build
from models.weapon import Weapon
from models.artifact import Artifact
import json

def score_weapon(weapon_type: str, role: str) -> int:
    scoring = {
        "Sword": {"DPS": 10, "Support": 5, "Healer": 3},
        "Bow": {"DPS": 8, "Support": 4, "Healer": 2},
        "Catalyst": {"DPS": 7, "Support": 6, "Healer": 5},
        "Polearm": {"DPS": 9, "Support": 4, "Healer": 2},
        "Claymore": {"DPS": 10, "Support": 3, "Healer": 2}
    }
    return scoring.get(weapon_type, {}).get(role, 0)

def score_artifact_set(artifact_role: str, character_role: str) -> int:
    # Logic: 10 points if roles match perfectly, 5 otherwise
    return 10 if artifact_role == character_role else 5

def generate_build(character: Character, db: Session):
    # 1. Check if build already exists
    existing_build = db.query(Build).filter(Build.character_id == character.id).first()
    if existing_build:
        return existing_build

    # 2. Select Weapon (with safety check)
    weapons = db.query(Weapon).all()
    if not weapons:
        # Fallback if DB is empty
        return Build(weapon="Default Sword", artifacts="[]", stats="{}", notes="No weapons in DB")

    best_weapon = max(weapons, key=lambda w: score_weapon(w.type, character.role))

    # 3. Select Artifacts
    artifacts = db.query(Artifact).all()
    best_artifacts = sorted(
        artifacts, 
        key=lambda a: score_artifact_set(a.role, character.role), 
        reverse=True
    )[:4]

    # 4. Generate Stats
    stats = {
        "ATK%": "35%", "CRIT Rate": "20%", "CRIT DMG": "50%"
    } if character.role == "DPS" else {
        "HP%": "30%", "Healing Bonus": "15%"
    }

    # 5. Save and Return
    new_build = Build(
        character_id=character.id,
        weapon=best_weapon.name,
        artifacts=json.dumps([a.name for a in best_artifacts]),
        stats=json.dumps(stats),
        notes=f"Build optimizada para {character.role}."
    )

    db.add(new_build)
    db.commit()
    db.refresh(new_build)
    return new_build