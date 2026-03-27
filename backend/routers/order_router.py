from fastapi import APIRouter, Depends, status

from backend.models.order_models import Order
from backend.schemas.orders import OrderCreate
from backend.services.order_service import OrderService

router = APIRouter(prefix="/orders", tags=["orders"])

@router.get("", response_model=Order)
async def get_order(order_id: int,service: OrderService = Depends(OrderService)):
    return service.find_by_id(order_id)

@router.post("", response_model=Order)
async def create_order(order_in: OrderCreate, service: OrderService = Depends(OrderService)):
    return service.create_order(order_in)

@router.delete("")
async def delete_order(order_id: int, service: OrderService = Depends(OrderService)):
    service.delete_by_id(order_id=order_id)