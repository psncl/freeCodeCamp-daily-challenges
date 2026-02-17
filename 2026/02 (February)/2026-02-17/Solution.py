def check_eligibility(athlete_weights: list[int], sled_weight: int) -> str:

    team_size = len(athlete_weights)
    sled_has_minimum_weight: bool = False
    sled_plus_athletes_are_under_maximum_weight: bool = False

    min_sled_weights: dict[int, int] = {
        1: 162,
        2: 170,
        4: 210
    }

    if sled_weight >= min_sled_weights[team_size]:
        sled_has_minimum_weight = True

    max_total_weights: dict[int, int] = {
        1: 247,
        2: 390,
        4: 630
    }
    
    if sum(athlete_weights) + sled_weight <= max_total_weights[team_size]:
        sled_plus_athletes_are_under_maximum_weight = True
    
    if sled_has_minimum_weight and sled_plus_athletes_are_under_maximum_weight:
        return "Eligible"
    else:
        return "Not Eligible"

## Tests

assert check_eligibility([78], 165) == "Eligible"
assert check_eligibility([80], 160) == "Not Eligible"
assert check_eligibility([80], 170) == "Not Eligible"
assert check_eligibility([85, 90], 170) == "Eligible"
assert check_eligibility([85, 95], 168) == "Not Eligible"
assert check_eligibility([112, 97], 185) == "Not Eligible"
assert check_eligibility([110, 102, 90, 106], 222) == "Eligible"
assert check_eligibility([106, 99, 90, 88], 205) == "Not Eligible"
assert check_eligibility([106, 99, 103, 96], 227) == "Not Eligible"