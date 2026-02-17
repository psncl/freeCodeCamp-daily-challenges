def check_eligibility(athlete_weights: list[int], sled_weight: int) -> str:

    team_size = len(athlete_weights)

    min_sled_weights: dict[int, int] = {
        1: 162,
        2: 170,
        4: 210
    }

    if sled_weight < min_sled_weights[team_size]:
        return "Not Eligible"

    max_total_weights: dict[int, int] = {
        1: 247,
        2: 390,
        4: 630
    }
    
    if sum(athlete_weights) + sled_weight > max_total_weights[team_size]:
        return "Not Eligible"
    
    return "Eligible"

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