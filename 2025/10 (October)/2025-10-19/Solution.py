import re

def extract_attributes(element: str) -> list[str]:

    pattern = r"\S+=\"[^\"]+\""
    matches = re.findall(pattern, element)

    if len(matches) == 0:
        return []

    replacements = { ord('='): ', ', ord('"'): "" }
    return [match.translate(replacements) for match in matches]

## Tests

assert extract_attributes('<span class="red"></span>') == ["class, red"]
assert extract_attributes('<meta charset="UTF-8" />') == ["charset, UTF-8"]
assert extract_attributes("<p>Lorem ipsum dolor sit amet</p>") == []
assert extract_attributes('<input name="email" type="email" required="true" />') == ["name, email", "type, email", "required, true"]
assert extract_attributes('<button id="submit" class="btn btn-primary">Submit</button>') == ["id, submit", "class, btn btn-primary"]