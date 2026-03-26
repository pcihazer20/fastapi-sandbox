import datetime
import uuid
from typing import Optional, List

from sqlmodel import Field, SQLModel

from backend.enums.payment_types import PaymentType


class PaymentBase(SQLModel):
    amount: float = 0.00
    currency: str = "USD"
    type: PaymentType = PaymentType.ach
    payer: str = ""
    payee: str = ""


class Payment(PaymentBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    transaction_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)


class PaymentCreate(PaymentBase):
    pass


class PaymentRead(PaymentBase):
    id: int
    transaction_id: uuid.UUID
    created_at: datetime.datetime


class PaymentUpdate(SQLModel):
    amount: Optional[float] = None
    currency: Optional[str] = None
    type: Optional[PaymentType] = None
    payer: Optional[str] = None
    payee: Optional[str] = None
