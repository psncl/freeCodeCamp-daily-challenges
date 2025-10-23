def classification(temp):
    temp_ranges = [
        (30000, "O"),
        (10000, "B"),
        (7500,  "A"),
        (6000,  "F"),
        (5200,  "G"),
        (3700,  "K"),
        (0,     "M"),
    ]

    for (temp_threshold, stellar_classification) in temp_ranges:
        if temp >= temp_threshold:
            return stellar_classification

## Tests

assert classification(5778) == "G"
assert classification(2400) == "M"
assert classification(9999) == "A"
assert classification(3700) == "K"
assert classification(3699) == "M"
assert classification(210000) == "O"
assert classification(6000) == "F"
assert classification(11432) == "B"