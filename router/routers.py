from typing import Optional

from fastapi import APIRouter
from fastapi import Depends

from config.database import get_db

from repository.user_reposytory import UserRepository
from repository.product_repository import ProductRepository
from repository.order_reposytory import OrderRepository
from repository.order_product_repository import OrderProductRepository

from schemas.schema import UserSchema, OrderSchema
from schemas.schema import ProductSchema

api_router = APIRouter()

"""    products    """


@api_router.post("/api/product/create/{productName}", tags=["Products"], response_model=ProductSchema | bool)
def create_product(product_name: str, product_price: int, db=Depends(get_db)):
    product_repo = ProductRepository(db)

    res = product_repo.create_product(product_name, product_price)
    return res


@api_router.get("/api/product/get-all", tags=["Products"], response_model=list[ProductSchema] | bool)
def get_all_products(db=Depends(get_db)):
    product_repo = ProductRepository(db)

    res = product_repo.get_all_products()
    return res


@api_router.get("/api/product/{productID}", tags=["Products"], response_model=ProductSchema | bool)
def get_product_by_id(product_id: int, db=Depends(get_db)):
    product_repo = ProductRepository(db)

    product_res = product_repo.get_product_by_id(product_id)
    return product_res


@api_router.patch("/api/product/{productID}", tags=["Products"], response_model=ProductSchema | bool)
def update_product_by_id(product_id: int, product_name: Optional[str] = None, product_price: Optional[int] = None, db=Depends(get_db)):
    product_repo = ProductRepository(db)

    res = product_repo.update_product_by_id(product_id=product_id,
                                            product_new_name=product_name,
                                            product_new_price=product_price)
    return res


@api_router.delete("/api/product/{productID}", tags=["Products"], response_model=ProductSchema | bool)
def delete_product_by_id(product_id: int, db=Depends(get_db)):
    product_repo = ProductRepository(db)

    res = product_repo.delete_product_by_id(product_id)
    return res


""""    users    """


@api_router.post("/api/user/create/{userName}", tags=["Users"], response_model=UserSchema | bool)
def create_user(user_name: str, db=Depends(get_db)):
    user_repo = UserRepository(db)

    res = user_repo.create_user(user_name)
    return res


@api_router.get("/api/user/get-all", tags=["Users"], response_model=list[UserSchema] | bool)
def get_all_users(db=Depends(get_db)):
    user_repo = UserRepository(db)

    res = user_repo.get_all_users()
    return res


@api_router.get("/api/user/{userID}", tags=["Users"], response_model=UserSchema | bool)
def get_user_by_id(user_id: int, db=Depends(get_db)):
    user_repo = UserRepository(db)

    user_res = user_repo.get_user_by_id(user_id)
    return user_res


@api_router.patch("/api/user/{userID}", tags=["Users"], response_model=UserSchema | bool)
def update_user_by_id(user_id: int, user_name: str, db=Depends(get_db)):
    user_repo = UserRepository(db)

    res = user_repo.update_user_by_id(user_id, user_name)
    return res


@api_router.delete("/api/user/{userID}", tags=["Users"], response_model=UserSchema | bool)
def delete_user_by_id(user_id: int, db=Depends(get_db)):
    user_repo = UserRepository(db)

    res = user_repo.delete_user_by_id(user_id)
    return res


"""    orders    """


@api_router.post("/api/order/create/{userID}", tags=["Orders"], response_model=OrderSchema | bool)
def create_order(user_id: int, db=Depends(get_db)):
    order_repo = OrderRepository(db)

    res = order_repo.create_order(user_id)
    return res


@api_router.get("/api/order/get-all", tags=["Orders"], response_model=list[OrderSchema] | bool)
def get_all_orders(db=Depends(get_db)):
    order_repo = OrderRepository(db)

    res = order_repo.get_all_orders()
    return res


@api_router.get("/api/order/get-all/{userID}", tags=["Orders"], response_model=list[OrderSchema] | bool)
def get_all_user_orders(user_id: int, db=Depends(get_db)):
    order_repo = OrderRepository(db)

    res = order_repo.get_all_user_orders(user_id)
    return res


@api_router.get("/api/order/{orderID}", tags=["Orders"], response_model=OrderSchema | bool)
def get_order_by_id(order_id: int, db=Depends(get_db)):
    order_repo = OrderRepository(db)

    res = order_repo.get_order_by_id(order_id)
    return res


@api_router.delete("/api/order{orderID}", tags=["Orders"], response_model=bool)
def delete_order_by_id(order_id: int, db=Depends(get_db)):
    order_repo = OrderRepository(db)

    res = order_repo.delete_order_by_id(order_id)
    return res


"""     order-products    """


@api_router.post("/api/orders-products/{userID}", tags=["OrdersProducts"], response_model=bool)
def add_product_to_order(order_id: int, product_id: int, db=Depends(get_db)):
    order_product_repo = OrderProductRepository(db)

    res = order_product_repo.add_product_to_order(order_id, product_id)
    return res


@api_router.delete("/api/orders-products/{userID}", tags=["OrdersProducts"], response_model=bool)
def delete_product_from_order(order_id: int, product_id: int, db=Depends(get_db)):
    order_product_repo = OrderProductRepository(db)

    res = order_product_repo.delete_product_from_order(order_id, product_id)
    return res


@api_router.get("/api/orders-products/get-all/{orderID}",
                 tags=["OrdersProducts"],
                 response_model=list[ProductSchema] | bool)
def get_all_products_from_order_by_order_id(order_id: int, db=Depends(get_db)):
    order_product_repo = OrderProductRepository(db)

    res = order_product_repo.get_all_products_from_order_by_order_id(order_id)
    return res

@api_router.get("/api/orders-products/total-price/{orderID}",
                 tags=["OrdersProducts"],
                 response_model=int | bool)
def count_total_order_price_by_order_id(order_id: int, db=Depends(get_db)):
    order_product_repo = OrderProductRepository(db)

    res = order_product_repo.count_total_order_price_by_order_id(order_id)
    return res

