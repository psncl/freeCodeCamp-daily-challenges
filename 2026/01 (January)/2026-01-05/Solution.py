from functools import partial

def tire_status(pressures_psi: list[float], range_bar: list[float]) -> list[str]:

    get_status = partial(tire_status_individual, pressure_range_bar = range_bar)
    return [get_status(pressure_psi) for pressure_psi in pressures_psi]

def tire_status_individual(pressure_psi: float, pressure_range_bar: list[float]) -> str:

    PSI_IN_ONE_BAR = 14.5038
    pressure_bar = pressure_psi / PSI_IN_ONE_BAR

    if pressure_bar > pressure_range_bar[1]:
        return "High"
    elif pressure_bar < pressure_range_bar[0]:
        return "Low"
    else:
        return "Good"

## Tests

assert tire_status([32, 28, 35, 29], [2, 3]) == ["Good", "Low", "Good", "Low"]
assert tire_status([32, 28, 35, 30], [2, 2.3]) == ["Good", "Low", "High", "Good"]
assert tire_status([29, 26, 31, 28], [2.1, 2.5]) == ["Low", "Low", "Good", "Low"]
assert tire_status([31, 31, 30, 29], [1.5, 2]) == ["High", "High", "High", "Good"]
assert tire_status([30, 28, 30, 29], [1.9, 2.1]) == ["Good", "Good", "Good", "Good"]