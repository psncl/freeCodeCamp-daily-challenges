# Space Week Day 4: Landing Spot

https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-07

In day four of Space Week, you are given a matrix of numbers (an array of arrays), representing potential landing spots for your rover. Find the safest landing spot based on the following rules:

- Each spot in the matrix will contain a number from `0-9`, inclusive.
- Any `0` represents a potential landing spot.
- Any number other than `0` is too dangerous to land. The higher the number, the more dangerous.
- The safest spot is defined as the `0` cell whose surrounding cells (up to 4 neighbors, ignore diagonals) have the lowest total danger.
- Ignore out-of-bounds neighbors (corners and edges just have fewer neighbors).
- Return the indices of the safest landing spot. There will always only be one safest spot.

For instance, given:

```python
[
  [1, 0],
  [2, 0]
]
```

Return `[0, 1]`, the indices for the `0` in the first array.

## Tests

1. `find_landing_spot([[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]])` should return `[2, 1]`.
1. `find_landing_spot([[1, 0], [2, 0]])` should return `[0, 1]`.
1. `find_landing_spot([[9, 0, 3], [7, 0, 4], [8, 0, 5]])` should return `[1, 1]`.
1. `find_landing_spot([[1, 2, 1], [0, 0, 2], [3, 0, 0]])` should return `[2, 2]`.
