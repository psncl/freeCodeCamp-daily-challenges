from itertools import groupby

def is_valid_nonogram(clue: list[int], cells: list[int]) -> bool:

    consecutive_ones = [len(list(v)) for (k, v) in groupby(cells) if k == 1]
    return clue == consecutive_ones

## Tests

assert is_valid_nonogram([3, 2], [1, 1, 1, 0, 1, 1]) == True
assert is_valid_nonogram([3, 2], [0, 1, 1, 1, 1, 1]) == False
assert is_valid_nonogram([1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1]) == False
assert is_valid_nonogram([1, 1, 1, 1], [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0]) == True
assert is_valid_nonogram([3, 2, 3], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0]) == True
assert is_valid_nonogram([3, 2, 3], [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]) == False