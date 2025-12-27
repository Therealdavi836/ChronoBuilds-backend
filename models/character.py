from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Character(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    element = Column(String)
    role = Column(String)
    weapon = Column(String)
    rarity = Column(Integer)
    
    builds = relationship("Build", back_populates="character")
