# Spam Detector

https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-27

Given a phone number in the format `"+A (BBB) CCC-DDDD"`, where each letter represents a digit as follows:

- `A` represents the country code and can be any number of digits.
- `BBB` represents the area code and will always be three digits.
- `CCC` and `DDDD` represent the local number and will always be three and four digits long, respectively.

Determine if it's a spam number based on the following criteria:

- The country code is greater than 2 digits long or doesn't begin with a zero (`0`).
- The area code is greater than 900 or less than 200.
- The sum of first three digits of the local number appears within last four digits of the local number.
- The number has the same digit four or more times in a row (ignoring the formatting characters).

## Tests

1. `is_spam("+0 (200) 234-0182")` should return `False`.
1. `is_spam("+091 (555) 309-1922")` should return `True`.
1. `is_spam("+1 (555) 435-4792")` should return `True`.
1. `is_spam("+0 (955) 234-4364")` should return `True`.
1. `is_spam("+0 (155) 131-6943")` should return `True`.
1. `is_spam("+0 (555) 135-0192")` should return `True`.
1. `is_spam("+0 (555) 564-1987")` should return `True`.
1. `is_spam("+00 (555) 234-0182")` should return `False`.
