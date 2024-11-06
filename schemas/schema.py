from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    name: str


class ProductSchema(BaseModel):
    id: int
    name: str
    price: int


class OrderSchema(BaseModel):
    id: int
    user_id: int

class BoolSchema(BaseModel):
    res: bool

class OrderProductSchema(BaseModel):
    id: int
    cart_id: int
    product_id: int
