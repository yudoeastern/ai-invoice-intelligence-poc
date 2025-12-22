def derive_dimensions(text: str) -> dict:
    t = text.lower()

    airline_code = None
    if "garuda" in t:
        airline_code = "GA"

    flight_type = "REGULAR"
    if "paket" in t or "charter" in t:
        flight_type = "CHARTER"

    route_type = "DOMESTIC"
    if "international" in t or "china" in t:
        route_type = "INTERNATIONAL"

    is_china_related = "china" in t

    return {
        "aircraft_type": None,
        "airline_code": airline_code,
        "route_type": route_type,
        "is_china_related": is_china_related,
        "flight_type": flight_type
    }
