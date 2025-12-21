def daylight_hours(latitude: int) -> int:

    # Map latitudes to daylight hours in ascending order.
    latitude_to_daylight: dict[int, int] = {
        -90: 24,
        -75: 23,
        -60: 21,
        -45: 15,
        -30: 13,
        -15: 12,
        0: 12,
        15:	11,
        30:	10,
        45:	9,
        60:	6,
        75:	2,
        90:	0,
    }

    if latitude in latitude_to_daylight:
        return latitude_to_daylight[latitude]

    # Sort the keys just in case the converting the keys() view object to a list changed the order.
    lat_keys = sorted(list(latitude_to_daylight.keys()))

    for i in range(len(lat_keys)):
        current = lat_keys[i]

        if latitude < current:
            # No need to check out of bounds below because latitude cannot be lower than -90.
            # Therefore, this if block will never be triggered when i = 0.
            prev = lat_keys[i-1]

            return latitude_to_daylight[current] if abs(current - latitude) < abs(prev - latitude) else latitude_to_daylight[prev]

## Tests

assert daylight_hours(45) == 9
assert daylight_hours(0) == 12
assert daylight_hours(-90) == 24
assert daylight_hours(-10) == 12
assert daylight_hours(23) == 10
assert daylight_hours(88) == 0
assert daylight_hours(-33) == 13
assert daylight_hours(70) == 2