# Truncate the Text

https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-04

Given a string, return it as-is if it's 20 characters or shorter. If it's longer than 20 characters, truncate it to the first 17 characters and append `"..."` to the end of it (so it's 20 characters total) and return the result.

## Tests

1. `truncate_text("Hello, world!")` should return `"Hello, world!"`.
1. `truncate_text("This string should get truncated.")` should return `"This string shoul..."`.
1. `truncate_text("Exactly twenty chars")` should return `"Exactly twenty chars"`.
1. `truncate_text(".....................")` should return `"...................."`.
