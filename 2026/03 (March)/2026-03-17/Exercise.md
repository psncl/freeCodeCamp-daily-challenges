# Anniversary Milestones

https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-17

Given an integer representing the number of years a couple has been married, return their most recent anniversary milestone according to this chart:

| Years Married | Milestone    |
| ------------- | ------------ |
| 1             | `"Paper"`    |
| 5             | `"Wood"`     |
| 10            | `"Tin"`      |
| 25            | `"Silver"`   |
| 40            | `"Ruby"`     |
| 50            | `"Gold"`     |
| 60            | `"Diamond"`  |
| 70            | `"Platinum"` |

- If they haven't reached the first milestone, return `"Newlyweds"`.

## Tests

1. `get_milestone(0)` should return `"Newlyweds"`.
1. `get_milestone(1)` should return `"Paper"`.
1. `get_milestone(8)` should return `"Wood"`.
1. `get_milestone(10)` should return `"Tin"`.
1. `get_milestone(26)` should return `"Silver"`.
1. `get_milestone(45)` should return `"Ruby"`.
1. `get_milestone(50)` should return `"Gold"`.
1. `get_milestone(64)` should return `"Diamond"`.
1. `get_milestone(71)` should return `"Platinum"`.
