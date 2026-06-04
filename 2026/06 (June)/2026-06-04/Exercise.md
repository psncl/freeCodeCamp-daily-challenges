# Schema Validator Part 4

https://www.freecodecamp.org/learn/daily-coding-challenge/2026-06-04

Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:

```ts
Roles = "user" | "creator" | "moderator" | "staff" | "admin"

{
  username: string,
  posts: number,
  verified: boolean,
  role: Roles,
  supporter?: boolean
}
```

- The pipe (`|`) symbol means "or". `role` must be one of the listed `Roles` values.
- The question mark (`?`) after `supporter` means that the field is optional, but is the specified type if it exists.
- Extra keys are allowed

## Tests

1. `is_valid_schema({"username": "vivian", "posts": 1, "verified": False, "role": "user", "supporter": True})` should return `True`.
1. `is_valid_schema({"username": "rudolph", "posts": 15, "verified": True, "role": "creator"})` should return `True`.
1. `is_valid_schema({"username": "hernandez", "posts": 35, "verified": True, "role": "moderator", "supporter": False, "followers": 55})` should return `True`.
1. `is_valid_schema({"username": "julia", "posts": 50, "verified": True, "role": "admin", "supporter": "true"})` should return `False`.
1. `is_valid_schema({"username": "bernard", "posts": 0, "verified": True, "role": "friend", "supporter": True})` should return `False`.
1. `is_valid_schema({"username": "felix", "posts": 40, "verified": "yes", "role": "staff", "supporter": False})` should return `False`.
1. `is_valid_schema({"username": "jimmy", "posts": True, "verified": False, "role": "creator", "supporter": True})` should return `False`.
1. `is_valid_schema({"username": True, "posts": 30, "verified": True, "role": "moderator", "supporter": False})` should return `False`.
