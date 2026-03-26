from fastapi import Depends
from sqlmodel import Session
from backend.database import get_session
from backend.models.order_models import Order


class OrderRepository:

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create_order(self, session: Session, order: Order) -> Order:
        session.add(order)
        session.commit()
        session.refresh(order)
        return order

    def find_by_id(self, order_id: int) -> type[Order] | None:
        return self.session.get(Order, order_id)

