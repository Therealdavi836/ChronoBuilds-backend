from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Build(Base):
    __tablename__ = "builds"
    id = Column(Integer, primary_key=True, index=True)
    character_id = Column(Integer, ForeignKey("characters.id"))
    weapon = Column(String)
    artifacts = Column(String)  
    stats = Column(String)      
    notes = Column(String)
    
    character = relationship("Character", back_populates="builds")
