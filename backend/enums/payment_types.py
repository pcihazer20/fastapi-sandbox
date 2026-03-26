from enum import Enum

class PaymentType(Enum):
    ach = 'ACH'
    credit = 'CREDIT'
    crypto = 'CRYPTO'
    refund = 'REFUND'
    paper = 'PAPER'
