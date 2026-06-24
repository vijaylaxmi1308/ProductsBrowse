from faker import Faker
from database import SessionLocal
from models import Product

fake = Faker()

db = SessionLocal()

categories = [
    "Electronics",
    "Books",
    "Fashion",
    "Sports",
    "Home"
]

for i in range(200000):

    product = Product(
        name=fake.word(),
        category=fake.random_element(categories),
        price=round(fake.random_number(digits=5), 2)
    )

    db.add(product)

db.commit()

print("200000 Products Added")