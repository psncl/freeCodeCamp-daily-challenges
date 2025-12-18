def create_board(dimensions: list[int]):
    
    rows, cols = dimensions[0], dimensions[1]
    matrix: list[list[str]] = [[""] * cols for _ in range(rows)]

    chars: dict[str, str] = {"X": "O", "O": "X"}

    for row in range(rows):
        for col in range(cols):
            # Base case where there is no cell right above to check against
            if row == 0:
                matrix[row][col] = "X" if col % 2 == 0 else "O"
            else:
                matrix[row][col] = chars[matrix[row - 1][col]]

    return matrix

## Tests

assert create_board([3, 3]) == [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]
assert create_board([6, 1]) == [["X"], ["O"], ["X"], ["O"], ["X"], ["O"]]
assert create_board([2, 10]) == [["X", "O", "X", "O", "X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X", "O", "X", "O", "X"]]
assert create_board([5, 4]) == [["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"]]


# Better version suggested by Claude that uses mathematical property of a checkerboard,
# where the cell value depends on the sum of row and column indices being even or odd.

def create_board_ai(dimensions: list[int]):

    rows, cols = dimensions[0], dimensions[1]
    matrix: list[list[str]] = [[""] * cols for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            matrix[row][col] = "X" if (row + col) % 2 == 0 else "O"

    return matrix

## Tests

assert create_board_ai([3, 3]) == [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]
assert create_board_ai([6, 1]) == [["X"], ["O"], ["X"], ["O"], ["X"], ["O"]]
assert create_board_ai([2, 10]) == [["X", "O", "X", "O", "X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X", "O", "X", "O", "X"]]
assert create_board_ai([5, 4]) == [["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"]]