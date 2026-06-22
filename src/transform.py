def transform(raw):
    state_raw = raw["state"][0]
    cities_raw = raw["cities"]

    state = {
        "name": state_raw["name"],
        "gasoline": float(state_raw["gasoline"]),
        "midGrade": float(state_raw["midGrade"]),
        "premium": float(state_raw["premium"]),
        "diesel": float(state_raw["diesel"]),
    }

    cities = [
        {
            "name": c["name"],
            "currency": c["currency"],
            "gasoline": float(c["gasoline"]),
            "midGrade": float(c["midGrade"]),
            "premium": float(c["premium"]),
            "diesel": float(c["diesel"]),
        }
        for c in cities_raw
    ]

    return state, cities
