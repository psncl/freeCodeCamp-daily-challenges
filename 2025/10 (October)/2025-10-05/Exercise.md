# Space Week Day 2: Exoplanet Search

https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-05

For the second day of Space Week, you are given a string where each character represents the luminosity reading of a star. Determine if the readings have detected an exoplanet using the transit method. The transit method is when a planet passes in front of a star, reducing its observed luminosity.

- Luminosity readings only comprise of characters `0-9` and `A-Z` where each reading corresponds to the following numerical values:
- Characters `0-9` correspond to luminosity levels `0-9`.
- Characters `A-Z` correspond to luminosity levels `10-35`.

A star is considered to have an exoplanet if any single reading is less than or equal to 80% of the average of all readings. For example, if the average luminosity of a star is 10, it would be considered to have a exoplanet if any single reading is 8 or less.

## Tests

1. `has_exoplanet("ZXXWYZXYWYXZEGZXWYZXYGEE")` should return `True`.
1. `has_exoplanet("665544554")` should return `False`.
1. `has_exoplanet("FGFFCFFGG")` should return `True`.
1. `has_exoplanet("MONOPLONOMONPLNOMPNOMP")` should return `False`.
1. `has_exoplanet("FREECODECAMP")` should return `True`.
1. `has_exoplanet("9AB98AB9BC98A")` should return `False`.
