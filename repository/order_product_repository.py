from sys import exception

from sqlalchemy import insert, select

from models.models import OrderProduct, Product


class OrderProductRepository:
    def __init__(self, db):
        self.db = db

    def add_product_to_order(self, order_id: int, product_id: int) -> bool:
        try:
            stmt = (
                insert(OrderProduct).
                values(
                    order_id=order_id,
                    product_id=product_id
                )
            )

            self.db.execute(stmt)
            self.db.commit()
            return True

        except exception():
            print(exception())
            return False

    def delete_product_from_order(self, order_id: int, product_id: int) -> bool:
        order = (self.db.query(OrderProduct)
                 .filter(OrderProduct.order_id == order_id,
                         OrderProduct.product_id == product_id)
                 .first())

        if order:
            self.db.delete(order)
            self.db.commit()
            return True

        else:
            return False

    def get_all_products_from_order_by_order_id(self, order_id: int) -> list[Product] | bool:
        stmt = (
            select(Product)
            .join(OrderProduct)
            .where(OrderProduct.order_id == order_id)
        )

        db_products = self.db.execute(stmt).scalars().all()

        if db_products:
            return db_products

        else:
            return False

    def count_total_order_price_by_order_id(self, order_id: int) -> int | bool:
        stmt = (
            select(Product.price)
            .join(OrderProduct)
            .where(OrderProduct.order_id == order_id)
        )

        db_products_prices = self.db.execute(stmt).scalars().all()

        if db_products_prices:
            return sum(db_products_prices)

        else:
            return False
