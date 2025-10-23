def hex_to_decimal(hex: str) -> int:

    hex_dec_mappings: dict[str, int] = {
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
    }

    decimal: int = 0

    for i, ch in enumerate(hex[::-1]):
        """
        Add up values of digits according to one's place, ten's place, etc.
        E.g. 15 becomes (5 * 16^0) + (1 * 16^1)
        """
        digit = int(ch) if ch.isdigit() else hex_dec_mappings[ch]
        decimal += digit * (16 ** i)

    return decimal

## Tests

assert hex_to_decimal("A") == 10
assert hex_to_decimal("15") == 21
assert hex_to_decimal("2E") == 46
assert hex_to_decimal("FF") == 255
assert hex_to_decimal("A3F") == 2623