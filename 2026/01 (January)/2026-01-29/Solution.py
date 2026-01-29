def separate_letters_and_numbers(s: str) -> str:

    result = s[0]

    for i in range(1, len(s)):
        if s[i].isdigit() != s[i-1].isdigit():
            result += "-"
        
        result += s[i]
    
    return result

## Tests

assert separate_letters_and_numbers("ABC123") == "ABC-123"
assert separate_letters_and_numbers("Route66") == "Route-66"
assert separate_letters_and_numbers("H3LL0W0RLD") == "H-3-LL-0-W-0-RLD"
assert separate_letters_and_numbers("a1b2c3d4") == "a-1-b-2-c-3-d-4"