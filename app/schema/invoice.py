from pydantic import BaseModel
from typing import Optional

class Amounts(BaseModel):
    total: Optional[int] = None
    down_payment: Optional[int] = None
    balance_due: Optional[int] = None
    tax: Optional[int] = None
    admin_fee: Optional[int] = None

class Invoice(BaseModel):
    vendor_name: Optional[str]
    invoice_number: Optional[str]
    invoice_date: Optional[str]
    currency: str = "IDR"
    amounts: Amounts
