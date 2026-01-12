from pydantic import BaseModel
from typing import Optional, List

class InvoiceItem(BaseModel):
    name: str
    quantity: Optional[int] = 1
    unit_price: Optional[int] = None
    total: Optional[int] = None

class Amounts(BaseModel):
    subtotal: Optional[int] = None
    tax: Optional[int] = None
    paid_amount: Optional[int] = None
    total: Optional[int] = None
    admin_fee: Optional[int] = None


class Invoice(BaseModel):
    vendor_name: Optional[str] = None
    invoice_number: Optional[str] = None
    invoice_date: Optional[str] = None
    currency: Optional[str] = "IDR"

    customer_name: Optional[str] = None
    status: Optional[str] = None
    items: Optional[List[InvoiceItem]] = None

    amounts: Amounts
