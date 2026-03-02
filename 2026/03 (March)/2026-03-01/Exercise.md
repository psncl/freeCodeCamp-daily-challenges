# Flattened

https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-01

Given an array, determine if it is flat.

- An array is flat if none of its elements are arrays.

## Tests

1. `is_flat([1, 2, 3, 4])` should return `True`.
1. `is_flat([1, [2, 3], 4])` should return `False`.
1. `is_flat([1, 0, False, True, "a", "b"])` should return `True`.
1. `is_flat(["a", [0], "b", True])` should return `False`.
1. `is_flat([1, [2, [3, [4, [5]]]], 6])` should return `False`.
