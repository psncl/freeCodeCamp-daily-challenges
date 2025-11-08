def can_post(message: str) -> str:

    lengths: list[tuple[int, str]] = [
        (40, "short post"),
        (80, "long post")
    ]

    return next((msg for (length, msg) in lengths if len(message) < length), "invalid post")

## Tests

assert can_post("Hello world") == "short post"
assert can_post("This is a longer message but still under eighty characters.") == "long post"
assert can_post("This message is too long to fit into either of the character limits for a social media post.") == "invalid post"