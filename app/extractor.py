from app.schema.invoice import Invoice, Amounts
from app.service.regex_extractor import (
    extract_vendor,
    extract_invoice_number,
    extract_invoice_date
)

def normalize_invoice(clean_text: str, amount_data: dict) -> Invoice:
    return Invoice(
        vendor_name=extract_vendor(clean_text),
        invoice_number=extract_invoice_number(clean_text),
        invoice_date=extract_invoice_date(clean_text),
        currency="IDR",
        amounts=Amounts(
            total=amount_data.get("total"),
            admin_fee=amount_data.get("admin_fee"),
            down_payment=amount_data.get("down_payment"),
            balance_due=amount_data.get("balance_due")
        )
    )
