import re

def string_sum(s: str) -> int:

    numbers = re.findall(r'\d+', s)
    return sum(int(num) for num in numbers)

## Tests

assert string_sum("3apples2bananas") == 5
assert string_sum("10cats5dogs2birds") == 17
assert string_sum("125344") == 125344
assert string_sum("a1b20c300") == 321
assert string_sum("a12b34c56d78e90f123g456h789i0j1k2l3m4n5") == 1653