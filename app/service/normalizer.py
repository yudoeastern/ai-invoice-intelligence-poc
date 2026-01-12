import re
from decimal import Decimal
from typing import Optional, Union

NumberLike = Union[str, int, float]

def parse_currency(value: Optional[NumberLike]) -> Optional[int]:
    if value is None:
        return None

    if isinstance(value, (int, float)):
        return int(value)

    if not isinstance(value, str):
        return None

    raw = value.strip()

    is_negative = "-" in raw

    # buang Rp, spasi, teks
    cleaned = re.sub(r"[^\d.,]", "", raw)

    # normalisasi format
    if "," in cleaned and "." in cleaned:
        cleaned = cleaned.replace(",", "")
    elif "." in cleaned:
        cleaned = cleaned.replace(".", "")

    try:
        amount = int(Decimal(cleaned))
        return -amount if is_negative else amount
    except Exception:
        return None
