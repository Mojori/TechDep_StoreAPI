from typing import List

from sqlalchemy.orm import relationship, MappedAsDataclass
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from config.database import Base, engine


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(unique=True)

    orders: Mapped[List["Order"]] = relationship(backref="orders.user_id", cascade="all, delete-orphan")


class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    
    name: Mapped[str] = mapped_column(unique=True)

    price: Mapped[int]


class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    products: Mapped[List[Product]] = relationship(secondary="order_product")


class OrderProduct(Base):
    __tablename__ = "order_product"
    id: Mapped[int] = mapped_column(primary_key=True)

    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), unique=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), unique=False)


User.metadata.create_all(engine)
Product.metadata.create_all(engine)
Order.metadata.create_all(engine)
OrderProduct.metadata.create_all(engine)
