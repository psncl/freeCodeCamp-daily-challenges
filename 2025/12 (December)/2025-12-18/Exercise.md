# Checkerboard

https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-18

Given an array with two numbers, the first being the number of rows and the second being the number of columns, return a matrix (an array of arrays) filled with `"X"` and `"O"` characters of the given size.

- The characters should alternate like a checkerboard.
- The top-left cell must always be `"X"`.

For example, given `[3, 3]`, return:

```python
[
  ["X", "O", "X"],
  ["O", "X", "O"],
  ["X", "O", "X"]
]
```

## Tests

1. `create_board([3, 3])` should return `[["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]`.
1. `create_board([6, 1])` should return `[["X"], ["O"], ["X"], ["O"], ["X"], ["O"]]`.
1. `create_board([2, 10])` should return `[["X", "O", "X", "O", "X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X", "O", "X", "O", "X"]]`.
1. `create_board([5, 4])` should return `[["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"]]`.
