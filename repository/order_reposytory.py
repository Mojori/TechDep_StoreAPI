from models.models import Order, User


class OrderRepository:
    def __init__(self, db):
        self.db = db

    def create_order(self, user_id: int) -> Order | bool:
        db_user = self.db.query(User).filter(User.id == user_id).first()

        if db_user:
            db_order = Order(user_id=user_id)
            self.db.add(db_order)
            self.db.commit()
            self.db.refresh(db_order)
            return db_order

        else:
            return False

    def get_all_orders(self) -> list[Order] | bool:
        db_orders = self.db.query(Order).all()

        if db_orders:
            return db_orders

        else:
            return False

    def get_all_user_orders(self, user_id: int) -> list[Order] | bool:
        db_order = self.db.query(Order).filter(Order.user_id == user_id).all()

        if db_order:
            return db_order

        else:
            return False

    def get_order_by_id(self, order_id: int) -> Order | bool:
        db_order = self.db.query(Order).filter(Order.id == order_id).first()

        if db_order:
            return db_order

        else:
            return False

    def delete_order_by_id(self, order_id: int) -> bool:
        db_order = self.db.query(Order).filter(Order.id == order_id).first()

        if db_order:
            self.db.delete(db_order)
            self.db.commit()
            return True

        else:
            return False
