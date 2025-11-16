import math

def count_rectangles(width: int, height: int) -> int:
    return math.comb(width + 1,  2) * math.comb(height + 1, 2)

"""
Solved through combinations:

If the rectangle has width of 3 and height of 2, in a grid form,
it will have (3+1) = 4 vertical grid lines, and (2+1) = 3 horizontal grid lines.
To create any rectangle on a grid, you need to select 2 vertical and 2 horizontal grid lines.

Therefore, with width of 3, we can select up to 4C2 (=6) vertical lines and 3C2 (=3) horizontal lines.
Multiply them to get the total number of smaller rectangles, which is 18.

Resulting formula: (W+1)C2 x (H+1)C2
"""

## Tests

assert count_rectangles(1, 3) == 6
assert count_rectangles(3, 2) == 18
assert count_rectangles(1, 2) == 3
assert count_rectangles(5, 4) == 150
assert count_rectangles(11, 19) == 12540