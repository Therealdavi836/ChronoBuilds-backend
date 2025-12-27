# models/weapon.py
from sqlalchemy import Column, Integer, String
from database import Base

class Weapon(Base):
    __tablename__ = "weapons"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    type = Column(String)  # Sword, Bow, Catalyst...
    main_stat = Column(String)
    sub_stat = Column(String)
    rarity = Column(Integer)
