def count_change(change: list[int]) -> str:

    total_cents = sum(change)
    return f"${(total_cents / 100):0.2f}"

## Tests

assert count_change([25, 10, 5, 1]) == "$0.41"
assert count_change([25, 10, 5, 1, 25, 10, 25, 1, 1, 10, 5, 25]) == "$1.43"
assert count_change([100, 25, 100, 1000, 5, 500, 2000, 25]) == "$37.55"
assert count_change([10, 5, 1, 10, 1, 25, 1, 1, 5, 1, 10]) == "$0.70"
assert count_change([1]) == "$0.01"
assert count_change([25, 25, 25, 25]) == "$1.00"