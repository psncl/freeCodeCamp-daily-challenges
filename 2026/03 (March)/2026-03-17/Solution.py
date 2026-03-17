def get_milestone(years: int) -> str:

    if years < 1:
        return "Newlyweds"

    anniversaries = {
        1: "Paper",
        5: "Wood",
        10: "Tin",
        25: "Silver",
        40: "Ruby",
        50: "Gold",
        60: "Diamond",
        70: "Platinum"
    }

    return anniversaries[max(year for year in anniversaries.keys() if year <= years)]

## Tests

assert get_milestone(0) == "Newlyweds"
assert get_milestone(1) == "Paper"
assert get_milestone(8) == "Wood"
assert get_milestone(10) == "Tin"
assert get_milestone(26) == "Silver"
assert get_milestone(45) == "Ruby"
assert get_milestone(50) == "Gold"
assert get_milestone(64) == "Diamond"
assert get_milestone(71) == "Platinum"