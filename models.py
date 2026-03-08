from pydantic import BaseModel
from typing import List
from datetime import datetime


class OrderItem(BaseModel):
    name: str
    size: str
    qty: int
    price: float


class OrderCreate(BaseModel):
    source: str
    table: str
    items: List[OrderItem]
    subtotal: float
    total: float


class Order(OrderCreate):
    id: str
    created_at: datetime
    status: str