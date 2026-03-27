from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel

# -------- Requests --------

class DemoCreate(BaseModel):
    description: Optional[str] = None
    amount: Decimal



# -------- Response --------

