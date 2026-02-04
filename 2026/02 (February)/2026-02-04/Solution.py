def truncate_text(text: str) -> str:

    max_length = 20
    suffix = "..."

    if len(text) <= max_length:
        return text
    else:
        return f"{text[:(max_length - len(suffix))]}{suffix}"

## Tests

assert truncate_text("Hello, world!") == "Hello, world!"
assert truncate_text("This string should get truncated.") == "This string shoul..."
assert truncate_text("Exactly twenty chars") == "Exactly twenty chars"
assert truncate_text(".....................") == "...................."