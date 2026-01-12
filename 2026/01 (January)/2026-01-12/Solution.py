def get_number_of_plants(field_size: float, unit: str, crop: str) -> float:

    SQUARE_METRES_FACTOR: dict[str, float] = {
        "acres": 4046.86,
        "hectares": 10_000
    }

    space_sq_metre_taken_by_plants: dict[str, float] = {
        "corn": 1,
        "wheat": 0.1,
        "soybeans": 0.5,
        "tomatoes": 0.25,
        "lettuce": 0.2
    }

    field_size_in_sq_metre: float = field_size * SQUARE_METRES_FACTOR[unit]

    return int(field_size_in_sq_metre / space_sq_metre_taken_by_plants[crop])

## Tests

assert get_number_of_plants(1, "acres", "corn") == 4046
assert get_number_of_plants(2, "hectares", "lettuce") == 100000
assert get_number_of_plants(20, "acres", "soybeans") == 161874
assert get_number_of_plants(3.75, "hectares", "tomatoes") == 150000
assert get_number_of_plants(16.75, "acres", "tomatoes") == 271139