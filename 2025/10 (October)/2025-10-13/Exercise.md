# 24 to 12

https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-13

Given a string representing a time of the day in the 24-hour format of `"HHMM"`, return the time in its equivalent 12-hour format of `"H:MM AM"` or `"H:MM PM"`.

- The given input will always be a four-digit string in 24-hour time format, from `"0000"` to `"2359"`.

## Tests

1. `to_12("1124")`should return`"11:24 AM"`.
1. `to_12("0900")`should return`"9:00 AM"`.
1. `to_12("1455")`should return`"2:55 PM"`.
1. `to_12("2346")`should return`"11:46 PM"`.
1. `to_12("0030")`should return`"12:30 AM"`.
