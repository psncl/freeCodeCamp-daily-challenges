def knight_moves(position: str) -> int:

    letter = position[0]
    number = int(position[1])

    possible_squares: list[str] = [
        f"{offset_letter(letter, 1)}{offset_number(number, 2)}",
        f"{offset_letter(letter, 1)}{offset_number(number, -2)}",
        f"{offset_letter(letter, 2)}{offset_number(number, 1)}",
        f"{offset_letter(letter, 2)}{offset_number(number, -1)}",
        f"{offset_letter(letter, -1)}{offset_number(number, 2)}",
        f"{offset_letter(letter, -1)}{offset_number(number, -2)}",
        f"{offset_letter(letter, -2)}{offset_number(number, 1)}",
        f"{offset_letter(letter, -2)}{offset_number(number, -1)}",
    ]

    return len(list(filter(valid_square, possible_squares)))

def valid_square(square: str) -> bool:

    first = square[0] >= 'A' and square[0] <= 'H'
    second = int(square[1:]) >= 1 and int(square[1:]) <= 8

    return first and second

def offset_letter(letter: str, offset: int) -> str:
    return chr(ord(letter[0]) + offset)

def offset_number(number: int, offset: int) -> int:
    return number + offset

## Tests

assert knight_moves("A1") == 2
assert knight_moves("D4") == 8
assert knight_moves("G6") == 6
assert knight_moves("B8") == 3
assert knight_moves("H3") == 4