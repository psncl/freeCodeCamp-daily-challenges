# String Mirror

https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-23

Given two strings, determine if the second string is a mirror of the first.

- A string is considered a mirror if it contains the same letters in reverse order.
- Treat uppercase and lowercase letters as distinct.
- Ignore all non-alphabetical characters.

## Tests

1. `isMirror("Hello World", "!dlroW !olleH")` should return `true`.
1. `isMirror("helloworld", "helloworld")` should return `false`.
1. `isMirror("Hello World", "dlroW olleH")` should return `true`.
1. `isMirror("RaceCar", "raCecaR")` should return `true`.
1. `isMirror("RaceCar", "RaceCar")` should return `false`.
1. `isMirror("Mirror", "rorrim")` should return `false`.
1. `isMirror("Hello World", "dlroW-olleH")` should return `true`.
