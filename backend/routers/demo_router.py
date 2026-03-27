from typing import List

from fastapi import APIRouter, Depends, status, HTTPException

from backend.models.payment_models import PaymentCreate, PaymentRead, PaymentUpdate
from backend.services.payment_service import PaymentService

router = APIRouter(prefix="/demo", tags=["demo"])



@router.get(path="")
async def get_data(data_id:str):
    message = f"This is a query parameter {data_id}"
    return {"message": message}
