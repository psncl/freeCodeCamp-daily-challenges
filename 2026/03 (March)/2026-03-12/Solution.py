def is_valid_domino_chain(dominoes: list[list[int]]) -> bool:
    return all(a[1] == b[0] for (a, b) in zip(dominoes, dominoes[1:]))

## Tests

assert is_valid_domino_chain([[1, 3], [3, 6], [6, 5]]) == True
assert is_valid_domino_chain([[6, 2], [3, 4], [4, 1]]) == False
assert is_valid_domino_chain([[2, 5], [5, 6], [5, 1]]) == False
assert is_valid_domino_chain([[4, 3], [3, 1], [1, 6], [6, 6], [6, 5], [5, 1], [1, 1], [1, 4], [4, 4], [4, 2]]) == True
assert is_valid_domino_chain([[2, 3], [3, 3], [3, 6], [6, 1], [1, 4], [3, 5], [5, 5], [5, 4], [4, 2], [2, 2]]) == False