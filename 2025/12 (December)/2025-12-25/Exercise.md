# Snowflake Generator

https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-25

Given a multi-line string that uses newline characters (`\n`) to represent a line break, return a new string where each line is mirrored horizontally and attached to the end of the original line.

- Mirror a line by reversing all of its characters, including spaces.

For example, given `"* \n *\n* "`, which logs to the console as:

```
*
 *
*
```

Return `"* *\n ** \n* *"`, which logs to the console as:

```
*  *
 **
*  *
```

Take careful note of the whitespaces in the given and returned strings. Be sure not to trim any of them.

## Tests

1. `generate_snowflake("* \n *\n* ")` should return `"* *\n ** \n* *"`.
1. `generate_snowflake("X=~")` should return `"X=~~=X"`.
1. `generate_snowflake(" X \n v \nX--=\n ^ \n X ")` should return `" X X \n v v \nX--==--X\n ^ ^ \n X X "`.
1. `generate_snowflake("* *\n * * \n* * *\n * * \n* *")` should return `"* ** *\n * * * * \n* * ** * *\n * * * * \n* ** *"`.
1. `generate_snowflake("* -\n * -\n* -")` should return `"* -- *\n * -- * \n* -- *"`.
