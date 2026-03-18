import re

def largest_number(s: str) -> float:

    separators = ",|!|\\?|:|;"
    return max(float(num) for num in re.split(separators, s))

## Tests

assert largest_number("1,2") == 2
assert largest_number("4;15:60,26?52!0") == 60
assert largest_number("-402,-1032!-569:-947;-633?-800!-1012;-402,-723?-8102!-3011") == -402
assert largest_number("12;-50,99.9,49.1!-10.1?88?16") == 99.9