from typing import Optional

from fastapi import Depends
from sqlalchemy import text
from sqlmodel import Session, select

from backend.database import get_session
from backend.models.payment_models import Payment


class PaymentRepository:
    """
    Data access layer for Payment.
    Analogous to a Spring @Repository — no business logic, no HTTP concerns.
    """

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def find_all(self, skip: int = 0, limit: int = 100) -> list[Payment]:
        return list(self.session.exec(select(Payment).offset(skip).limit(limit)).all())

    def find_by_id(self, payment_id: int) -> Optional[Payment]:
        return self.session.get(Payment, payment_id)

    def save(self, payment: Payment) -> Payment:
        self.session.add(payment)
        self.session.commit()
        self.session.refresh(payment)
        return payment

    def delete(self, payment: Payment) -> None:
        self.session.delete(payment)
        self.session.commit()

    def stats_by_type(self) -> list[dict]:
        """Custom SQL query: totals and averages grouped by payment type."""
        result = self.session.exec(
            text("""
                SELECT
                    type,
                    COUNT(*)    AS count,
                    SUM(amount) AS total_amount,
                    AVG(amount) AS avg_amount
                FROM payment
                GROUP BY type
                ORDER BY total_amount DESC
            """)
        )
        return [dict(row) for row in result.mappings().all()]
