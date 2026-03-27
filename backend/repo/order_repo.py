from fastapi import Depends
from sqlmodel import Session
from backend.database import get_session
from backend.models.order_models import Order


class OrderRepository:

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create_order(self, order: Order) -> Order:
        self.session.add(order)
        self.session.commit()
        self.session.refresh(order)
        return order

    def find_by_id(self, order_id: int) -> Order | None:
        return self.session.get(Order, order_id)

    def delete_by_id(self, order_id: int) -> None:
         order = self.session.get(Order, order_id)
         self.session.delete(order)
         self.session.commit()



