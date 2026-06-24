from sqlalchemy import Column, Integer, String, Float,Index
from sqlalchemy.orm import declarative_base
from sqlalchemy import DateTime
from datetime import datetime


Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    price = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    __table_args__ = (
    Index("idx_created_at", "created_at"),
    Index("idx_category", "category"),
) 