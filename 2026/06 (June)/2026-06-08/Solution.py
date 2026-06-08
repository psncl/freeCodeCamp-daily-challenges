from typing import Literal

CITIES_OFFSETS: dict[str, int] = {
    "Los Angeles": -8,
    "New York": -5,
    "London": 0,
    "Istanbul": 3,
    "Dubai": 4,
    "Hong Kong": 8,
    "Tokyo": 9
}

def get_jet_lag_hours(departure_city: str, arrival_city: str, flight_duration: int, direction: Literal["west", "east"]) -> float:

    timezone_difference = abs(CITIES_OFFSETS[arrival_city] - CITIES_OFFSETS[departure_city])
    direction_multiplier = 1.5 if direction == "east" else 1.0
    jet_lag_hours = timezone_difference + (flight_duration * 0.1) * direction_multiplier
    return round(jet_lag_hours, 1)

## Tests

assert get_jet_lag_hours("Istanbul", "Hong Kong", 10, "east") == 6.5
assert get_jet_lag_hours("London", "New York", 8, "west") == 5.8
assert get_jet_lag_hours("Hong Kong", "Tokyo", 4, "east") == 1.6
assert get_jet_lag_hours("Dubai", "London", 7, "west") == 4.7
assert get_jet_lag_hours("Los Angeles", "Hong Kong", 15, "west") == 17.5
assert get_jet_lag_hours("Tokyo", "Dubai", 9, "west") == 5.9
assert get_jet_lag_hours("New York", "Istanbul", 10, "east") == 9.5