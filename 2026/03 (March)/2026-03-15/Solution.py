from typing import Literal
from collections import Counter

def get_captured_value(pieces: list[str]) -> int | Literal["Checkmate"]:

    if "K" not in pieces:
        return "Checkmate"
    
    # Map chess pieces to a tuple of (quantity, value)
    pieces_inventory: dict[str, tuple[int, int]] = {
        "P": (8, 1),
        "R": (2, 5),
        "N": (2, 3),
        "B": (2, 3),
        "Q": (1, 9),
        "K": (1, 0),
    }

    piece_counts_on_board = Counter(pieces)
    # {'P': 6, 'R': 2, 'N': 1, 'B': 1, 'Q': 1, 'K': 1}

    return sum(
            (total_count - piece_counts_on_board.get(piece, 0)) * value
            for piece, (total_count, value) in pieces_inventory.items()
        )

## Tests

assert get_captured_value(["P", "P", "P", "P", "P", "P", "R", "R", "N", "B", "Q", "K"]) == 8
assert get_captured_value(["P", "P", "P", "P", "P", "R", "B", "K"]) == 26
assert get_captured_value(["K", "P", "P", "N", "P", "P", "R", "P", "B", "P", "N", "B"]) == 16
assert get_captured_value(["P", "Q", "N", "P", "P", "B", "K", "P", "R", "R", "P", "P", "B", "P"]) == 4
assert get_captured_value(["P", "K"]) == 38
assert get_captured_value(["N", "P", "P", "B", "K", "P", "Q", "N", "P", "P", "R", "R", "P", "P", "P", "B"]) == 0
assert get_captured_value(["N", "P", "P", "B", "P", "R", "Q", "P", "P", "P", "B"]) == "Checkmate"