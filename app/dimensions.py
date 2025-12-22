def derive_dimensions(text: str) -> dict:
    t = text.lower()

    airline_code = "GA" if "garuda" in t else None
    flight_type = "CHARTER" if "paket trip" in t or "wisata" in t else "REGULAR"
    route_type = "INTERNATIONAL" if "china" in t else "DOMESTIC"
    is_china_related = "china" in t

    return {
        "aircraft_type": None,
        "airline_code": airline_code,
        "route_type": route_type,
        "is_china_related": is_china_related,
        "flight_type": flight_type
    }
