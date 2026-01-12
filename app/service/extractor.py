import re
from datetime import datetime
from app.schema.invoice import Invoice, Amounts
from app.service.normalizer import parse_currency


BLACKLIST_VENDOR = {"receipt", "recept", "invoice", "paid"}

def _pick_first(arr):
    return arr[0] if arr else None

def clean_vendor(v: str | None) -> str | None:
    if not v:
        return None

    v_clean = v.lower().strip()

    # buang kata UI / noise
    for bad in ["receipt", "recept", "invoice", "paid"]:
        v_clean = v_clean.replace(bad, "").strip()

    if not v_clean:
        return None

    # normalisasi nama vendor umum
    if "traveloka" in v_clean:
        return "Traveloka"

    return v_clean.title()


def clean_invoice_number(values: list[str]) -> str | None:
    for v in values:
        m = re.search(r"\d{8,}", v)
        if m:
            return m.group(0)
    return None

def normalize_date(v: str | None) -> str | None:
    if not v:
        return None

    v = v.strip()[:11]

    try:
        dt = datetime.strptime(v, "%d %b %Y")
        return dt.strftime("%Y-%m-%d")
    except Exception:
        return None


def normalize_invoice(llm_data: dict) -> Invoice:
    total = None
    # if llm_data.get("payment_amount_candidates"):
    #     total = llm_data["payment_amount_candidates"][0]
    # elif llm_data.get("total_candidates"):
    #     total = llm_data["total_candidates"][0]
    if llm_data.get("payment_amount_candidates"):
        total = llm_data["payment_amount_candidates"][0]
    elif llm_data.get("total_candidates"):
        total = llm_data["total_candidates"][0]
    elif llm_data.get("subtotal_candidates"):
        total = llm_data["subtotal_candidates"][0]



    vendor = None
    for v in llm_data.get("vendor_name_candidates", []):
        vendor = clean_vendor(v)
        if vendor:
            break

    return Invoice(
        vendor_name=vendor,
        invoice_number=clean_invoice_number(
            llm_data.get("invoice_number_candidates", [])
        ),
        invoice_date=normalize_date(
            _pick_first(llm_data.get("invoice_date_candidates", []))
        ),
        currency="IDR",
        amounts=Amounts(
            total=parse_currency(total),
            admin_fee=parse_currency(
                _pick_first(llm_data.get("admin_fee_candidates", []))
            )
        )
    )
