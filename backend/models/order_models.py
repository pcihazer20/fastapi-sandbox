from decimal import Decimal
from typing import List, Optional
import uuid
import datetime

from sqlmodel import SQLModel, Field, Relationship


class Order(SQLModel, table=True):
    __tablename__ = "order"
    id: Optional[int] = Field(default=None, primary_key=True)
    # External-safe identifier (better than exposing DB id)
    number: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        index=True,
        nullable=False,
        unique=True
    )
    description: Optional[str] = Field(default=None, nullable=True)
    # Consider Decimal for money in real systems
    total: Decimal = Field(nullable=False)
    # 🔥 Aggregate root relationship
    items: List["OrderItem"] = Relationship(
        back_populates="order",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
            "lazy": "selectin"  # avoids N+1 issues
        }
    )
    created_at: datetime.datetime = Field(
        default_factory=datetime.datetime.utcnow,
        nullable=False
    )


class OrderItem(SQLModel, table=True):
    __tablename__ = "order_item"

    id: Optional[int] = Field(default=None, primary_key=True)
    description: Optional[str] = Field(default=None, nullable=True)
    amount: Decimal = Field(nullable=False)
    # 🔥 REQUIRED FK (no orphan records)
    order_id: int = Field(foreign_key="order.id", nullable=False, index=True)
    order: Optional["Order"] = Relationship(back_populates="items")
    created_at: datetime.datetime = Field(
        default_factory=datetime.datetime.utcnow,
        nullable=False
    )


class OrderItemCreate(SQLModel):
    description: Optional[str] = None
    amount: Decimal


class OrderCreate(SQLModel):
    description: Optional[str] = None
    total: Decimal
    items: List[OrderItemCreate]

