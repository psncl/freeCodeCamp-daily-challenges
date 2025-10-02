def to_decimal(binary):
    return sum(int(digit) * (2**index) for index, digit in enumerate(reversed(binary)))