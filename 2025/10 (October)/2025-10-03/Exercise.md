# P@ssw0rd Str3ngth!

Given a password string, return `"weak"`, `"medium"`, or `"strong"` based on the strength of the password.

A password is evaluated according to the following rules:

- It is at least 8 characters long.
- It contains both uppercase and lowercase letters.
- It contains at least one number.
- It contains at least one special character from this set: `!`, `@`, `#`, `$`, `%`, `^`, `&`, or `*`.

Return `"weak"` if the password meets fewer than two of the rules. Return `"medium"` if the password meets 2 or 3 of the rules. Return `"strong"` if the password meets all 4 rules.

## Tests

- `check_strength("C0d3&Fun!")` should return `"strong"`.
- `check_strength("123456")` should return `"weak"`.
- `check_strength("pass!!!")` should return `"weak"`.
- `check_strength("Qwerty")` should return `"weak"`.
- `check_strength("PASSWORD")` should return `"weak"`.
- `check_strength("PASSWORD!")` should return `"medium"`.
- `check_strength("PassWord%^!")` should return `"medium"`.
- `check_strength("qwerty12345")` should return `"medium"`.
- `check_strength("PASSWORD!")` should return `"medium"`.
- `check_strength("PASSWORD!")` should return `"medium"`.
- `check_strength("S3cur3P@ssw0rd")` should return `"strong"`.
