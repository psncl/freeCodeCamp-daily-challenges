from typing import Literal

def get_hill_rating(drop: int, distance: int, hill_type: str) -> Literal["Black", "Blue", "Green"]:

    hill_type_to_steepness_factor: dict[str, float] = {
        "Downhill": 1.2,
        "Slalom": 0.9,
        "Giant Slalom": 1.0
    }

    steepness = drop / distance
    steepness *= hill_type_to_steepness_factor[hill_type]

    if steepness > 0.25:
        return "Black"
    elif steepness > 0.1:
        return "Blue"
    else:
        return "Green"

## Tests

assert get_hill_rating(95, 900, "Slalom") == "Green"
assert get_hill_rating(620, 2800, "Downhill") == "Black"
assert get_hill_rating(420, 1680, "Giant Slalom") == "Blue"
assert get_hill_rating(250, 3000, "Downhill") == "Green"
assert get_hill_rating(110, 900, "Slalom") == "Blue"
assert get_hill_rating(380, 1500, "Giant Slalom") == "Black"