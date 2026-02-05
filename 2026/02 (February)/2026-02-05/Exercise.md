# Pocket Change

https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-05

Given an array of integers representing the coins in your pocket, with each integer being the value of a coin in cents, return the total amount in the format `"$D.CC"`.

- 100 cents equals 1 dollar.
- In the return value, include a leading zero for amounts less than one dollar and always exactly two digits for the cents.

## Tests

1. `count_change([25, 10, 5, 1])` should return `"$0.41"`.
1. `count_change([25, 10, 5, 1, 25, 10, 25, 1, 1, 10, 5, 25])` should return `"$1.43"`.
1. `count_change([100, 25, 100, 1000, 5, 500, 2000, 25])` should return `"$37.55"`.
1. `count_change([10, 5, 1, 10, 1, 25, 1, 1, 5, 1, 10])` should return `"$0.70"`.
1. `count_change([1])` should return `"$0.01"`.
1. `count_change([25, 25, 25, 25])` should return `"$1.00"`.
