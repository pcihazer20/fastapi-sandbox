from typing import List

from fastapi import APIRouter, Depends, status, HTTPException

from backend.models.payment_models import PaymentCreate, PaymentRead, PaymentUpdate
from backend.services.payment_service import PaymentService

router = APIRouter(prefix="/payments", tags=["payments"])


@router.post("", response_model=PaymentRead, status_code=status.HTTP_201_CREATED)
async def create_payment(data: PaymentCreate, service: PaymentService = Depends(PaymentService)):
    return service.create(data)


@router.get("", response_model=List[PaymentRead])
async def list_payments(
    skip: int = 0,
    limit: int = 100,
    service: PaymentService = Depends(PaymentService),
):
    return service.get_all(skip=skip, limit=limit)


@router.get("/stats/by-type")
async def payment_stats_by_type(service: PaymentService = Depends(PaymentService)):
    return service.get_stats_by_type()


@router.get("/{payment_id}", response_model=PaymentRead)
async def get_payment(payment_id: int, service: PaymentService = Depends(PaymentService)):
    return service.get_by_id(payment_id)


@router.patch("/{payment_id}", response_model=PaymentRead)
async def update_payment(
    payment_id: int,
    data: PaymentUpdate,
    service: PaymentService = Depends(PaymentService),
):
    return service.update(payment_id, data)


@router.delete("/{payment_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_payment(payment_id: int, service: PaymentService = Depends(PaymentService)):
    service.delete(payment_id)
