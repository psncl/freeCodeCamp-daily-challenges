from typing import Any

def is_flat(arr: list[Any]) -> bool:
    return not any(isinstance(item, list) for item in arr)

## Tests

assert is_flat([1, 2, 3, 4]) == True
assert is_flat([1, [2, 3], 4]) == False
assert is_flat([1, 0, False, True, "a", "b"]) == True
assert is_flat(["a", [0], "b", True]) == False
assert is_flat([1, [2, [3, [4, [5]]]], 6]) == False