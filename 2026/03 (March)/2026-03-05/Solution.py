def smallest_gap(s: str) -> str:

    matches: list[str] = []

    for i in range(len(s) - 2):
        offset = i + 1
        matched_index = s[offset:].find(s[i])

        if matched_index != -1:
            matches.append(s[offset : matched_index + offset])

    return min(matches, key=len)

## Tests

assert smallest_gap("ABCDAC") == "DA"
assert smallest_gap("racecar") == "e"
assert smallest_gap("A{5e^SD*F4i!o#q6e&rkf(po8|we9+kr-2!3}=4") == "#q6e&rkf(p"
assert smallest_gap("Hello World") == ""
assert smallest_gap("The quick brown fox jumps over the lazy dog.") == "fox"