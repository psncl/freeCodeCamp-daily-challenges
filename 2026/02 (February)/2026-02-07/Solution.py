def get_landing_stance(start_stance: str, rotation: int) -> str:

    opposite = {"Regular": "Goofy", "Goofy": "Regular"}

    flips = abs(rotation) // 180

    if flips % 2 == 0:
        return start_stance
    else:
        return opposite[start_stance]

## Tests

assert get_landing_stance("Regular", 90) == "Regular"
assert get_landing_stance("Regular", 180) == "Goofy"
assert get_landing_stance("Goofy", -270) == "Regular"
assert get_landing_stance("Regular", 2340) == "Goofy"
assert get_landing_stance("Goofy", 2160) == "Goofy"
assert get_landing_stance("Goofy", -540) == "Regular"