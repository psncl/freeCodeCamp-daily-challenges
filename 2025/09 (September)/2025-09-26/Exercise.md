# Caught Speeding

https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-26

Given an array of numbers representing the speed at which vehicles were observed traveling, and a number representing the speed limit, return an array with two items, the number of vehicles that were speeding, followed by the average amount beyond the speed limit of those vehicles.

- If there were no vehicles speeding, return `[0, 0]`.

## Tests

1. `speeding([50, 60, 55], 60)` should return `[0, 0]`.
1. `speeding([58, 50, 60, 55], 55)` should return `[2, 4]`.
1. `speeding([61, 81, 74, 88, 65, 71, 68], 70)` should return `[4, 8.5]`.
1. `speeding([100, 105, 95, 102], 100)` should return `[2, 3.5]`.
1. `speeding([40, 45, 44, 50, 112, 39], 55)` should return `[1, 57]`.
