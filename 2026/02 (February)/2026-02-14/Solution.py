def get_difficulty(track: str) -> str:

    points = 0
    opposite_directions = {"L": "R", "R": "L"}

    for i in range(1, len(track)):
        if track[i] == "S":
            continue
        
        points += 15 if track[i-1] == opposite_directions.get(track[i]) else 5
    
    if points > 200:
        return "Hard"
    elif points >= 101:
        return "Medium"
    else:
        return "Easy"

## Tests

assert get_difficulty("SLSLLSRRLSRLRL") == "Easy"
assert get_difficulty("LLRSLRLRSLLRLRSLRRLRSRLLS") == "Hard"
assert get_difficulty("SRRRRLSLLRLRSSRLSRL") == "Medium"
assert get_difficulty("LSRLRLSRLRLSLRSLRLLRLSRLRLRSL") == "Hard"
assert get_difficulty("SLLSSLRLSLSLRSLSSLRL") == "Medium"
assert get_difficulty("SRSLSRSLSRRSLSRSRSLSRLSRSR") == "Easy"