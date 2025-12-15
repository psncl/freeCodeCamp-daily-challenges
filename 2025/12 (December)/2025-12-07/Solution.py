def compress_string(sentence: str) -> str:
    occurences: list[list[str | int]] = []

    for word in sentence.split(" "):
        if len(occurences) == 0:
            occurences.append([word, 1])
        elif occurences[-1][0] == word:
            occurences[-1][1] += 1
        else:
            occurences.append([word, 1])

    string = ""
    for occurence in occurences:
        prefix = occurence[0]
        suffix = "" if occurence[1] == 1 else f"({occurence[1]})"
        string += f"{prefix}{suffix} "

    return string.strip()

## Tests

assert compress_string("yes yes yes please") == "yes(3) please"
assert compress_string("I have have have apples") == "I have(3) apples"
assert compress_string("one one three and to the the the the") == "one(2) three and to the(4)"
assert compress_string("route route route route route route tee tee tee tee tee tee") == "route(6) tee(6)"