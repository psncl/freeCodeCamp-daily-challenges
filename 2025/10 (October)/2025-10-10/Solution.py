# Version completely written by me
def launch_fuel(payload: int) -> float:

    FUEL_DELTA = 1.0
    FUEL_RATE = 5

    init_fuel_needed: float = payload / FUEL_RATE
    updated_fuel_needed = (payload + init_fuel_needed) / FUEL_RATE

    while updated_fuel_needed - init_fuel_needed >= FUEL_DELTA:
        init_fuel_needed = updated_fuel_needed
        updated_fuel_needed = (payload + init_fuel_needed) / FUEL_RATE

    return round(updated_fuel_needed, 1)


# After improvements suggested by AI
def launch_fuel_AI(payload: int) -> float:

    FUEL_DELTA = 1.0
    FUEL_RATE = 5

    fuel_needed: float = payload / FUEL_RATE

    while True:
        updated_fuel_needed = (payload + fuel_needed) / FUEL_RATE

        if updated_fuel_needed - fuel_needed < FUEL_DELTA:
            return round(updated_fuel_needed, 1)
        fuel_needed = updated_fuel_needed


# Recursive version. Makes the most logical sense when modeling it in real world terms
def launch_fuel_recursive(payload: int, prev_fuel_needed: float = 0.0) -> float:

    FUEL_DELTA = 1.0
    FUEL_RATE = 5

    if prev_fuel_needed == 0.0:
        prev_fuel_needed = payload / FUEL_RATE

    updated_fuel_needed = (payload + prev_fuel_needed) / FUEL_RATE

    if updated_fuel_needed - prev_fuel_needed < FUEL_DELTA:
        return round(updated_fuel_needed, 1)

    return launch_fuel_recursive(payload, updated_fuel_needed)

## Tests

assert launch_fuel(50) == 12.4
assert launch_fuel(500) == 124.8
assert launch_fuel(243) == 60.7
assert launch_fuel(11000) == 2749.8
assert launch_fuel(6214) == 1553.4