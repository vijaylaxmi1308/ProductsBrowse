from database import SessionLocal
from models import Product
from fastapi import FastAPI
from database import engine
from models import Base
from typing import Optional
from sqlalchemy import func
from datetime import datetime

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Project Working"}

@app.get("/products")
def get_products(category: Optional[str] = None,
                 cursor: Optional[str] = None):

    db = SessionLocal()
    query = db.query(Product)
    if category:
        query=query.filter(
            func.lower(Product.category) == category.lower()
        )
    if cursor:
        cursor_date = datetime.fromisoformat(cursor)
        query = query.filter(
            Product.created_at < cursor_date
        )

    products = (query.order_by(Product.created_at.desc()).limit(20).all())

    return {
    "products": products,
    "next_cursor": products[-1].created_at.isoformat()
    if products
    else None
}

@app.get("/delete-all")
def delete_all():

    db = SessionLocal()

    db.query(Product).delete()

    db.commit()

    return {"message": "All Products Deleted"}

@app.get("/count")
def count_products():

    db = SessionLocal()

    count = db.query(Product).count()

    return {"total_products": count}