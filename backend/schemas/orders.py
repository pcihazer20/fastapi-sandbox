from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel

# -------- Requests --------
class OrderItemCreate(BaseModel):
    description: Optional[str] = None
    amount: Decimal


class OrderCreate(BaseModel):
    description: Optional[str] = None
    total: Decimal
    items: List[OrderItemCreate]


# -------- Responses --------
class OrderItemRead(BaseModel):
    id: int
    description: Optional[str]
    amount: Decimal


class OrderRead(BaseModel):
    id: int
    number: str
    description: Optional[str]
    total: Decimal
    items: List[OrderItemRead]