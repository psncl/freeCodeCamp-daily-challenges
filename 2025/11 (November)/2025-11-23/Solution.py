def count_characters(sentence: str) -> list[str]:

    occurrences: dict[str, int] = {}

    for ch in sentence.lower():
        if ch.isalpha():
            occurrences[ch] = occurrences.get(ch, 0) + 1

    sorted_occurrences = dict(sorted(occurrences.items()))

    return [f"{k} {v}" for k, v in sorted_occurrences.items()]


# More Pythonic way with Counter

from collections import Counter

def count_characters_counter(sentence: str) -> list[str]:
    chars = (ch for ch in sentence.lower() if ch.isalpha())
    occurrences = Counter(chars)

    return [f"{k} {v}" for k, v in sorted(occurrences.items())]

## Tests

assert count_characters("hello world") == ["d 1", "e 1", "h 1", "l 3", "o 2", "r 1", "w 1"]
assert count_characters("I love coding challenges!") == ["a 1", "c 2", "d 1", "e 3", "g 2", "h 1", "i 2", "l 3", "n 2", "o 2", "s 1", "v 1"]
assert count_characters("// TODO: Complete this challenge ASAP!") == ["a 3", "c 2", "d 1", "e 4", "g 1", "h 2", "i 1", "l 3", "m 1", "n 1", "o 3", "p 2", "s 2", "t 3"]

assert count_characters_counter("hello world") == ["d 1", "e 1", "h 1", "l 3", "o 2", "r 1", "w 1"]
assert count_characters_counter("I love coding challenges!") == ["a 1", "c 2", "d 1", "e 3", "g 2", "h 1", "i 2", "l 3", "n 2", "o 2", "s 1", "v 1"]
assert count_characters_counter("// TODO: Complete this challenge ASAP!") == ["a 3", "c 2", "d 1", "e 4", "g 1", "h 2", "i 1", "l 3", "m 1", "n 1", "o 3", "p 2", "s 2", "t 3"]