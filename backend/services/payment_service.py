from fastapi import Depends, HTTPException

from backend.models.payment_models import Payment, PaymentCreate, PaymentUpdate
from backend.repositories.payment_repo import PaymentRepository


class PaymentService:
    """
    Business logic layer for Payment.
    Analogous to a Spring @Service — orchestrates repository calls and enforces
    domain rules (e.g. raising 404 when a resource is not found).
    """

    def __init__(self, repo: PaymentRepository = Depends(PaymentRepository)):
        self.repo = repo

    def get_all(self, skip: int = 0, limit: int = 100) -> list[Payment]:
        return self.repo.find_all(skip=skip, limit=limit)

    def get_by_id(self, payment_id: int) -> Payment:
        payment = self.repo.find_by_id(payment_id)
        if not payment:
            raise HTTPException(status_code=404, detail="Payment not found")
        return payment

    def create(self, data: PaymentCreate) -> Payment:
        payment = Payment.model_validate(data)
        return self.repo.save(payment)

    def update(self, payment_id: int, data: PaymentUpdate) -> Payment:
        payment = self.get_by_id(payment_id)
        payment.sqlmodel_update(data.model_dump(exclude_unset=True))
        return self.repo.save(payment)

    def delete(self, payment_id: int) -> None:
        payment = self.get_by_id(payment_id)
        self.repo.delete(payment)

    def get_stats_by_type(self) -> list[dict]:
        return self.repo.stats_by_type()
