import math

def infected(days: int) -> int:

    computers = 0

    for day in range(days + 1):
        if day == 0:
            computers += 1
            continue
        else:
            computers *= 2
        
        if day % 3 == 0:
            patched = math.ceil(computers * 0.2)
            computers -= patched
        
    return computers

## Tests

assert infected(1) == 2
assert infected(3) == 6
assert infected(8) == 152
assert infected(17) == 39808
assert infected(25) == 5217638