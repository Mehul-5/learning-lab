from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Evidence(Base):
    __tablename__ = 'evidence_items'

    id = Column(Integer, primary_key=True)
    description = Column(String)