def count_perfect_cubes(a: int, b: int) -> int:
    return sum(1 for num in range(min(a,b), max(a,b) + 1) if is_perfect_cube(num))

def is_perfect_cube(num: int) -> bool:
    number = abs(num)
    return round(number ** (1/3)) ** 3 == number

## Tests

assert count_perfect_cubes(3, 30) == 2
assert count_perfect_cubes(1, 30) == 3
assert count_perfect_cubes(30, 0) == 4
assert count_perfect_cubes(-64, 64) == 9
assert count_perfect_cubes(9214, -8127) == 41