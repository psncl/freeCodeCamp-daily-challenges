def one_hundred(chars: str) -> str:

    string: str = chars * (100 // len(chars))

    remaining_count: int = 100 % len(chars)
    if remaining_count != 0:
        string += chars[:remaining_count]

    return string

## Tests

assert one_hundred("One hundred ") == "One hundred One hundred One hundred One hundred One hundred One hundred One hundred One hundred One "
assert one_hundred("freeCodeCamp ") == "freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeC"
assert one_hundred("daily challenges ") == "daily challenges daily challenges daily challenges daily challenges daily challenges daily challenge"
assert one_hundred("!") == "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"