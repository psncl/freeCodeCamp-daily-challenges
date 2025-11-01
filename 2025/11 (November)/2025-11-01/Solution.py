def verify(message: str, key: str, signature: int) -> bool:
    return (sum_values(message) + sum_values(key)) == signature

def letter_value(letter: str) -> int:

    if letter.islower():
        return ord(letter) - ord('a') + 1
    else:
        return ord(letter) - ord('A') + letter_value('z') + 1

def sum_values(string: str) -> int:
    return sum([letter_value(ch) for ch in string if ch.isalpha()])

## Tests

assert verify("foo", "bar", 57) == True
assert verify("foo", "bar", 54) == False
assert verify("freeCodeCamp", "Rocks", 238) == True
assert verify("Is this valid?", "No", 210) == False
assert verify("Is this valid?", "Yes", 233) == True
assert verify("Check out the freeCodeCamp podcast,", "in the mobile app", 514) == True