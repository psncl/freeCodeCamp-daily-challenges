def send_message(route: list[int]) -> float:

    SPEED = 300_000
    total_distance = sum(route)

    DELAY = 0.5
    satellite_count = len(route[0:-1])

    total_time_taken = (total_distance / SPEED) + (satellite_count * DELAY)

    return round(total_time_taken, 4)

## Tests

assert send_message([300000, 300000]) == 2.5
assert send_message([384400, 384400]) == 3.0627
assert send_message([54600000, 54600000]) == 364.5
assert send_message([1000000, 500000000, 1000000]) == 1674.3333
assert send_message([10000, 21339, 50000, 31243, 10000]) == 2.4086
assert send_message([802101, 725994, 112808, 3625770, 481239]) == 21.1597