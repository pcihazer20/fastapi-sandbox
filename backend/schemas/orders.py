from typing import List, Optional
from sqlmodel import SQLModel

# -------- Requests --------
class OrderItemCreate(SQLModel):
    description: Optional[str] = None
    amount: float


class OrderCreate(SQLModel):
    description: Optional[str] = None
    total: float
    items: List[OrderItemCreate]


# -------- Responses --------
class OrderItemRead(SQLModel):
    id: int
    description: Optional[str]
    amount: float


class OrderRead(SQLModel):
    id: int
    number: str
    description: Optional[str]
    total: float
    items: List[OrderItemRead]