from fastapi import Depends
from sqlmodel import Session
from backend.database import get_session
from backend.models.order_models import Order


class DemoRepository:

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session



