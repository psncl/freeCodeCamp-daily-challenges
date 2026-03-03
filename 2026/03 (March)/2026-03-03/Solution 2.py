# Alternate solution, which I feel is how I would solve
# a mathematical problem like this in real life, with pen and paper.
#
# Find the first perfect cube in the range, take its cube root x,
# and keep cubing x + 1, x + 2, ..., until you cross the upper bound.

def count_perfect_cubes(a: int, b: int) -> int:
    lower = min(a, b)
    higher = max(a, b)
    count = 0

    global perfect_cube

    for num in range(lower, higher + 1):
        if is_perfect_cube(num):
            perfect_cube = cbrt(num)
            count += 1
            break

    perfect_cube += 1
    while perfect_cube ** 3 <= higher:
        count += 1
        perfect_cube += 1

    return count

def is_perfect_cube(num: int) -> bool:
    return cbrt(num) ** 3 == num

def cbrt(num: int) -> int:
    value = round(abs(num) ** (1 / 3))
    return value if num >= 0 else -value

## Tests

assert count_perfect_cubes(3, 30) == 2
assert count_perfect_cubes(1, 30) == 3
assert count_perfect_cubes(30, 0) == 4
assert count_perfect_cubes(-64, 64) == 9
assert count_perfect_cubes(9214, -8127) == 41