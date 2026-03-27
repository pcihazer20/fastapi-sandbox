from decimal import Decimal
from typing import List, Optional
import uuid
import datetime

from sqlmodel import SQLModel, Field, Relationship

class Demo(SQLModel, table=True):
    __tablename__ = "demo"
    id: Optional[int] = Field(default=None, primary_key=True)
