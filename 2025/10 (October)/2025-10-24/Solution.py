def dive(map: list[list[str]], coordinates: list[int]) -> str:

    unfound_count = 0

    for row in map:
        for column in row:
            if column == "O":
                unfound_count += 1

    dive_location_contents = map[coordinates[0]][coordinates[1]]

    if dive_location_contents == "-":
        return "Empty"
    elif dive_location_contents == "O" and unfound_count <= 1:
        return "Recovered"
    else:
        return "Found"

## Tests

assert dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 1]) == "Recovered"
assert dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 0]) == "Empty"
assert dive([[ "-", "X"], [ "-", "O"], [ "-", "O"]], [1, 1]) == "Found"
assert dive([[ "-", "-", "-"], [ "X", "O", "X"], [ "-", "-", "-"]], [1, 2]) == "Found"
assert dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [2, 0]) == "Recovered"
assert dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [1, 2]) == "Empty"