def sock_pairs(pairs: int, cycles: int) -> int:

    socks = pairs * 2

    wash_cycle_patterns: list[tuple[int, int]] = [
        (2, -1),
        (3, 1),
        (5, -1),
        (10, 2)
    ]

    for (cycle, sock_inc_or_dec) in wash_cycle_patterns:
        multiplier = cycles // cycle
        socks += multiplier * sock_inc_or_dec
    
    if socks < 0:
        socks = 0
    
    return socks // 2

## Tests

assert sock_pairs(2, 5) == 1
assert sock_pairs(1, 2) == 0
assert sock_pairs(5, 11) == 4
assert sock_pairs(6, 25) == 3
assert sock_pairs(1, 8) == 0