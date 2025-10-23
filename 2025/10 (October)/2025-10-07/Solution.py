from functools import partial

Matrix = list[list[int]] #for type hinting

def find_landing_spot(matrix: Matrix) -> list[int]:

    landing_spots: set[tuple[int, int]] = set()
    rows = [row for row in matrix]

    for row_index, row in enumerate(rows):
        for column_index, column in enumerate(row):
            if column == 0:
                landing_spots.add((row_index, column_index))

    return list(min(landing_spots, key=partial(calculate_total_danger, matrix_arg=matrix)))

def column_in_bounds(index: int, arr: list[int]) -> bool:
    return index >= 0 and index < len(arr)

def calculate_total_danger(indices: tuple[int, int], matrix_arg: Matrix) -> int:

        danger = 0
        indices_to_check: list[tuple[int, int]] = [
            (indices[0] + 1, indices[1]),
            (indices[0] - 1, indices[1]),
            (indices[0], indices[1] + 1),
            (indices[0], indices[1] - 1),
        ]

        for (row, column) in indices_to_check:
            row_in_bounds = row >= 0 and row < len(matrix_arg)
            if row_in_bounds and column_in_bounds(column, matrix_arg[0]): #All rows have same number of columns, so hardcoding matrix_arg[0] works
                danger += matrix_arg[row][column]
        
        return danger

## Tests

assert find_landing_spot([[1, 0], [2, 0]]) == [0, 1]
assert find_landing_spot([[9, 0, 3], [7, 0, 4], [8, 0, 5]]) == [1, 1]
assert find_landing_spot([[1, 2, 1], [0, 0, 2], [3, 0, 0]]) == [2, 2]
assert find_landing_spot([[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]]) == [2, 1]