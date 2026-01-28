type IntOrStr = int | str
type RecursiveList[T] = T | list["RecursiveList[T]"]

def flatten(arr: list[RecursiveList[IntOrStr]]) -> list[IntOrStr]:

    result: list[IntOrStr] = []

    for item in arr:
        if isinstance(item, (int, str)):
            result.append(item)
        elif isinstance(item, list):
            flattened = flatten(item)
            result.extend(flattened)
    
    return result

## Tests

assert flatten([1, [2, 3], 4]) == [1, 2, 3, 4]
assert flatten([5, [4, [3, 2]], 1]) == [5, 4, 3, 2, 1]
assert flatten(["A", [[[["B"]]]], "C"]) == ["A", "B", "C"]
assert flatten([["L", "M", "N"], ["O", ["P", "Q", ["R", ["S", ["T", "U"]]]]], "V", ["W", ["X", ["Y", ["Z"]]]]]) == ["L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
assert flatten([["red", ["blue", ["green", ["yellow", ["purple"]]]]], "orange", ["pink", ["brown"]]]) == ["red","blue","green","yellow","purple","orange","pink","brown"]