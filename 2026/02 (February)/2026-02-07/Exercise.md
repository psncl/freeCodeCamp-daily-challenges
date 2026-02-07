# 2026 Winter Games Day 2: Snowboarding

https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-07

Given a snowboarder's starting stance and a rotation in degrees, determine their landing stance.

- A snowboarder's stance is either `"Regular"` or `"Goofy"`.
- Trick rotations are multiples of 90 degrees. Positive indicates clockwise rotation, and negative indicate counter-clockwise rotation.
- The landing stance flips every 180 degrees of rotation.

For example, given `"Regular"` and `90`, return `"Regular"`. Given `"Regular"` and `180` degrees, return `"Goofy"`.

## Tests

1. `get_landing_stance("Regular", 90)` should return `"Regular"`.
1. `get_landing_stance("Regular", 180)` should return `"Goofy"`.
1. `get_landing_stance("Goofy", -270)` should return `"Regular"`.
1. `get_landing_stance("Regular", 2340)` should return `"Goofy"`.
1. `get_landing_stance("Goofy", 2160)` should return `"Goofy"`.
1. `get_landing_stance("Goofy", -540)` should return `"Regular"`.
