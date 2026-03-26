from fastapi import Depends, HTTPException

from backend.models.order_models import Order, OrderCreate, OrderItem
from backend.repositories.order_repo import OrderRepository


class OrderService:
    def __init__(self, repo: OrderRepository = Depends(OrderRepository)):
        self.repo = repo

    def create_order(self, order_in: OrderCreate) -> Order:
        calculated_total = sum(item.amount for item in order_in.items)
        if round(calculated_total, 2) != round(order_in.total, 2):
            raise HTTPException(
                status_code=400,
                detail="Total does not match sum of items"
            )

        order = Order(
            description=order_in.description,
            total=order_in.total,
            items=[
                OrderItem(description=item.description, amount=item.amount)
                for item in order_in.items
            ]
        )
        return self.repo.create_order(self.repo.session, order)

    def get_by_id(self, order_id: int) -> Order:
        order = self.repo.find_by_id(order_id)
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
        return order
