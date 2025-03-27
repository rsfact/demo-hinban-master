from sqlalchemy import Column, Integer, String
from .database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ex_id = Column(String(50), nullable=False, index=True, comment="客先キー")
    in_id = Column(String(50), nullable=False, index=True, comment="社内キー")
