def goldilocks_zone(mass: float) -> list[float]:

    luminosity = mass ** 3.5
    start_zone = 0.95 * (luminosity ** (1/2))
    end_zone = 1.37 * (luminosity ** (1/2))

    return [round(n, 2) for n in [start_zone, end_zone]]

## Tests

assert goldilocks_zone(1) == [0.95, 1.37]
assert goldilocks_zone(0.5) == [0.28, 0.41]
assert goldilocks_zone(6) == [21.85, 31.51]
assert goldilocks_zone(3.7) == [9.38, 13.52]
assert goldilocks_zone(20) == [179.69, 259.13]