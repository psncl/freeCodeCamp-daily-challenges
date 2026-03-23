def has_no_repeats(s: str) -> bool:
    return all(a != b for (a,b) in zip(s, s[1:]))

## Tests

assert has_no_repeats("hi world") == True
assert has_no_repeats("hello world") == False
assert has_no_repeats("abcdefghijklmnopqrstuvwxyz") == True
assert has_no_repeats("freeCodeCamp") == False
assert has_no_repeats("The quick brown fox jumped over the lazy dog.") == True
assert has_no_repeats("Mississippi") == False