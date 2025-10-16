def count(text: str, parameter: str) -> int:

    count = 0

    for i in range(0, len(text)):
        substring_length = i + len(parameter)
        if parameter == text[i:substring_length]:
            count += 1

    return count

## Tests

assert count('abcdefg', 'def') == 1
assert count('hello', 'world') == 0
assert count('mississippi', 'iss') == 2
assert count('she sells seashells by the seashore', 'sh') == 3
assert count('101010101010101010101', '101') == 10