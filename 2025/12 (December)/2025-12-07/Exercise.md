# String Compression

https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-07

Given a string sentence, return a compressed version of the sentence where consecutive duplicate words are replaced by the word followed with the number of times it repeats in parentheses.

- Only consecutive duplicates are compressed.
- Words are separated by single spaces.

For example, given `"yes yes yes please"`, return `"yes(3) please"`.

## Tests

1. `compress_string("yes yes yes please")` should return `"yes(3) please"`.
1. `compress_string("I have have have apples")` should return `"I have(3) apples"`.
1. `compress_string("one one three and to the the the the")` should return `"one(2) three and to the(4)"`.
1. `compress_string("route route route route route route tee tee tee tee tee tee")` should return `"route(6) tee(6)"`.
