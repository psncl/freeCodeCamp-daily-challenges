# Weekday Finder

https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-06

Given a string date in the format `YYYY-MM-DD`, return the day of the week.

Valid return days are:

- `"Sunday"`
- `"Monday"`
- `"Tuesday"`
- `"Wednesday"`
- `"Thursday"`
- `"Friday"`
- `"Saturday"`

Be sure to ignore time zones.

## Tests

1. `get_weekday("2025-11-06")` should return `Thursday`.
1. `get_weekday("1999-12-31")` should return `Friday`.
1. `get_weekday("1111-11-11")` should return `Saturday`.
1. `get_weekday("2112-12-21")` should return `Wednesday`.
1. `get_weekday("2345-10-01")` should return `Monday`.
