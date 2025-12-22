from schema import Invoice, Amounts

def normalize_invoice(llm_json: dict) -> Invoice:
    return Invoice(
        vendor_name=llm_json.get("vendor_name"),
        invoice_number=llm_json.get("invoice_number"),
        invoice_date=llm_json.get("invoice_date"),
        amounts=Amounts(**llm_json.get("amounts", {}))
    )
