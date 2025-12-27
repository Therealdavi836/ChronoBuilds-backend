from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base

class Build(Base):
    __tablename__ = "builds"

    id = Column(Integer, primary_key=True, index=True)
    weapon = Column(String)
    artifacts = Column(Text) # Storing JSON as string
    stats = Column(Text)     # Storing JSON as string
    notes = Column(Text)
    
    # Foreign Key to characters table
    character_id = Column(Integer, ForeignKey("characters.id"))
    
    # Relationship back to Character
    character = relationship("Character", back_populates="builds")