from typing import Optional

from models.models import Product
from sqlalchemy import update


class ProductRepository:
    def __init__(self, db):
        self.db = db

    def create_product(self, product_name: str, product_price: int) -> Product | bool:
        db_product = self.db.query(Product).filter(Product.name == product_name).first()

        if not db_product:
            db_product = Product(name=product_name, price=product_price)
            self.db.add(db_product)
            self.db.commit()
            self.db.refresh(db_product)
            return db_product

        else:
            return False

    def get_all_products(self) -> list[Product] | bool:
        db_products = self.db.query(Product).all()

        if db_products:
            return db_products

        else:
            return False

    def get_product_by_id(self, product_id: int) -> Product | bool:
        db_product = self.db.query(Product).filter(Product.id == product_id).first()

        if db_product:
            return db_product
        else:
            return False

    def update_product_by_id(self, product_id: int,
                             product_new_price: Optional[int],
                             product_new_name: Optional[str]) -> Product | bool:

        db_product = self.db.query(Product).filter(Product.id == product_id).first()

        if not product_new_name: product_new_name = db_product.name
        if not product_new_price: product_new_price = db_product.price

        if db_product:
            stmt = (
                update(Product).
                where(Product.id == product_id).
                values(name=product_new_name, price=product_new_price)
            )
            self.db.execute(stmt)
            self.db.commit()
            self.db.refresh(db_product)

            return db_product

        else:
            return False

    def delete_product_by_id(self, product_id: int) -> bool:
        db_product = self.db.query(Product).filter(Product.id == product_id).first()

        if db_product:
            self.db.delete(db_product)
            self.db.commit()
            return True

        else:
            return False

