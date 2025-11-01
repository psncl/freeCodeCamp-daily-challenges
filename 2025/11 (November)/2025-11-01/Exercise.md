# Signature Validation

https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-01

Given a message string, a secret key string, and a signature number, determine if the signature is valid using this encoding method:

- Letters in the message and secret key have these values:
  - `a` to `z` have values `1` to `26` respectively.
  - `A` to `Z` have values `27` to `52` respectively.
- All other characters have no value.
- Compute the signature by taking the sum of the message plus the sum of the secret key.

For example, given the message `"foo"` and the secret key `"bar"`, the signature would be `57`:

## Tests

1. `verify("foo", "bar", 57)` should return `True`.
1. `verify("foo", "bar", 54)` should return `False`.
1. `verify("freeCodeCamp", "Rocks", 238)` should return `True`.
1. `verify("Is this valid?", "No", 210)` should return `False`.
1. `verify("Is this valid?", "Yes", 233)` should return `True`.
1. `verify("Check out the freeCodeCamp podcast,", "in the mobile app", 514)` should return `True`.
