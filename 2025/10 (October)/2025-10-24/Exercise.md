# Hidden Treasure

https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-24

Given a 2D array representing a map of the ocean floor that includes a hidden treasure, and an array with the coordinates (`[row, column]`) for the next dive of your treasure search, return `"Empty"`, `"Found"`, or `"Recovered"` using the following rules:

- The given 2D array will contain exactly one unrecovered treasure, which will occupy multiple cells.

- Each cell in the 2D array will contain one of the following values:

  - `"-"`: No treasure.
  - `"O"`: A part of the treasure that has not been found.
  - `"X"`: A part of the treasure that has already been found.

- If the dive location has no treasure, return `"Empty"`.

- If the dive location finds treasure, but at least one other part of the treasure remains unfound, return `"Found"`.

- If the dive location finds the last unfound part of the treasure, return `"Recovered"`.

For example, given:

```python
[
  [ "-", "X"],
  [ "-", "X"],
  [ "-", "O"]
]
```

And `[2, 1]` for the coordinates of the dive location, return `"Recovered"` because the dive found the last unfound part of the treasure.

## Tests

1. `dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 1])` should return `"Recovered"`.
1. `dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 0])` should return `"Empty"`.
1. `dive([[ "-", "X"], [ "-", "O"], [ "-", "O"]], [1, 1])` should return `"Found"`.
1. `dive([[ "-", "-", "-"], [ "X", "O", "X"], [ "-", "-", "-"]], [1, 2])` should return `"Found"`.
1. `dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [2, 0])` should return `"Recovered"`.
1. `dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [1, 2])` should return `"Empty"`.
