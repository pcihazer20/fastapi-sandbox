from fastapi import APIRouter, Depends, status

from backend.models.order_models import Order, OrderCreate
from backend.services.order_service import OrderService

router = APIRouter(prefix="/orders", tags=["orders"])

@router.get("")
async def get_order():
    return {"message": "Hello World"}

@router.post("", response_model=Order)
def create_order(order_in: OrderCreate, service: OrderService = Depends(OrderService)):
    return service.create_order(order_in)