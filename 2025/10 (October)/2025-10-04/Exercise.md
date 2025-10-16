# Space Week Day 1: Stellar Classification

https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-04

October 4th marks the beginning of World Space Week. The next seven days will bring you astronomy-themed coding challenges.

For today's challenge, you are given the surface temperature of a star in Kelvin (K) and need to determine its stellar classification based on the following ranges:

- `"O"`: 30,000 K or higher
- `"B"`: 10,000 K - 29,999 K
- `"A"`: 7,500 K - 9,999 K
- `"F"`: 6,000 K - 7,499 K
- `"G"`: 5,200 K - 5,999 K
- `"K"`: 3,700 K - 5,199 K
- `"M"`: 0 K - 3,699 K
- Return the classification of the given star.

## Tests

1. `classification(5778)` should return `"G"`.
1. `classification(2400)` should return `"M"`.
1. `classification(9999)` should return `"A"`.
1. `classification(3700)` should return `"K"`.
1. `classification(3699)` should return `"M"`.
1. `classification(210000)` should return `"O"`.
1. `classification(6000)` should return `"F"`.
1. `classification(11432)` should return `"B"`.
