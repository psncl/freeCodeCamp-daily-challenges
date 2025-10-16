# CSV Header Parser

https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-28

Given the first line of a comma-separated values (CSV) file, return an array containing the headings.

- The first line of a CSV file contains headings separated by commas.
- Remove any leading or trailing whitespace from each heading.

## Tests

1. `get_headings("name,age,city")` should return `["name", "age", "city"]`.
1. `get_headings("first name,last name,phone")` should return `["first name", "last name", "phone"]`.
1. `get_headings("username , email , signup date ")` should return `["username", "email", "signup date"]`.
