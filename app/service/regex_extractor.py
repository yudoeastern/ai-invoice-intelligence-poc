import re
from datetime import datetime

def extract_vendor(text: str) -> str | None:
    # Traveloka hard rule (POC scope)
    if re.search(r"traveloka", text, re.IGNORECASE):
        return "Traveloka"
    return None


def extract_invoice_number(text: str) -> str | None:
    # Ambil angka panjang (Traveloka receipt)
    m = re.search(r"#?\s*(\d{10,})", text)
    if m:
        return m.group(1)
    return None


def extract_invoice_date(text: str) -> str | None:
    # Cari format "07 Sep 2018"
    m = re.search(
        r"(\d{1,2}\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{4})",
        text,
        re.IGNORECASE
    )
    if not m:
        return None

    dt = datetime.strptime(m.group(1), "%d %b %Y")
    return dt.strftime("%Y-%m-%d")
