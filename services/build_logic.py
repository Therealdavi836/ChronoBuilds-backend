from models.character import Character
from models.build import Build
from sqlalchemy.orm import Session
import json

# Ejemplo simple de puntuación de armas y artefactos según rol
weapon_scores = {
    "Sword": {"DPS": 10, "Support": 5},
    "Bow": {"DPS": 8, "Support": 4},
    "Catalyst": {"DPS": 7, "Support": 6}
}

artifact_sets = {
    "Gladiator": {"DPS": 10, "Support": 5},
    "Noblesse": {"DPS": 6, "Support": 10},
    "Wanderer": {"DPS": 7, "Support": 6}
}

def generate_build(character: Character, db: Session):
    # Verificar si la build ya existe
    existing_build = db.query(Build).filter(Build.character_id == character.id).first()
    if existing_build:
        return existing_build

    # Seleccionar arma y artefactos con mejor puntuación según rol
    role = character.role  # DPS, Support, etc.
    best_weapon = max(weapon_scores, key=lambda w: weapon_scores[w].get(role, 0))
    best_artifacts = sorted(artifact_sets, key=lambda a: artifact_sets[a].get(role, 0), reverse=True)[:4]

    # Crear estadísticas simples
    stats = {"ATK%": "30%", "CRIT Rate": "15%", "CRIT DMG": "50%"}

    # Guardar la build en la base de datos
    build = Build(
        character_id=character.id,
        weapon=best_weapon,
        artifacts=json.dumps(best_artifacts),
        stats=json.dumps(stats),
        notes=f"Build generada para maximizar el rol {role} del personaje."
    )
    db.add(build)
    db.commit()
    db.refresh(build)
    return build
