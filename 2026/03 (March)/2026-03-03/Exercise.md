# Perfect Cube Count

https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-03

Given two integers, determine how many perfect cubes exist in the range between and including the two numbers.

- The lower number is not garanteed to be the first argument.
- A number is a perfect cube if there exists an integer (`n`) where `n * n * n = number`. For example, 27 is a perfect cube because `3 * 3 * 3 = 27`.

## Tests

1. `count_perfect_cubes(3, 30)` should return `2`.
1. `count_perfect_cubes(1, 30)` should return `3`.
1. `count_perfect_cubes(30, 0)` should return `4`.
1. `count_perfect_cubes(-64, 64)` should return `9`.
1. `count_perfect_cubes(9214, -8127)` should return `41`.
