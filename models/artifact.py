# models/artifact.py
from sqlalchemy import Column, Integer, String
from database import Base

class Artifact(Base):
    __tablename__ = "artifacts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    set_name = Column(String)
    main_stat = Column(String)
    sub_stat = Column(String)
    role = Column(String)  # DPS, Support, Healer