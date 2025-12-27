from database import SessionLocal, engine, Base
from models.weapon import Weapon
from models.artifact import Artifact
from models.character import Character

# 1. Create the tables
Base.metadata.create_all(bind=engine)

def seed():
    db = SessionLocal()
    
    # Add some basic Weapons
    if db.query(Weapon).count() == 0:
        weapons = [
            Weapon(name="Wolf's Gravestone", type="Claymore"),
            Weapon(name="Aquila Favonia", type="Sword"),
            Weapon(name="Amos' Bow", type="Bow"),
            Weapon(name="Lost Prayer", type="Catalyst"),
            Weapon(name="Primordial Jade Spear", type="Polearm")
        ]
        db.add_all(weapons)
    
    # Add some basic Artifacts
    if db.query(Artifact).count() == 0:
        artifacts = [
            Artifact(name="Gladiator's Finale", role="DPS"),
            Artifact(name="Noblesse Oblige", role="Support"),
            Artifact(name="Maiden Beloved", role="Healer"),
            Artifact(name="Viridescent Venerer", role="Support")
        ]
        db.add_all(artifacts)

    db.commit()
    db.close()
    print("Database tables created and seeded successfully!")

if __name__ == "__main__":
    seed()