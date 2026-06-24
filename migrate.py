from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Product

# OLD SQLITE DATABASE
sqlite_engine = create_engine("sqlite:///products.db")
SQLiteSession = sessionmaker(bind=sqlite_engine)

# NEW NEON DATABASE
neon_engine = create_engine(
    "postgresql://neondb_owner:npg_rZIzdP1n8vKh@ep-misty-sound-aifimltc.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require"
)
NeonSession = sessionmaker(bind=neon_engine)

sqlite_db = SQLiteSession()
neon_db = NeonSession()

products = sqlite_db.query(Product).all()

print(f"Found {len(products)} products")

for product in products:
    new_product = Product(
        name=product.name,
        category=product.category,
        price=product.price,
        created_at=product.created_at,
        updated_at=product.updated_at
    )

    neon_db.add(new_product)

neon_db.commit()

print("Migration completed!")