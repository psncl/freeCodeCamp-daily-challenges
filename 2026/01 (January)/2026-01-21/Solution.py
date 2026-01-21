import re

def parse_inline_code(markdown: str):

    pattern = r"`([^`]+)`"
    return re.sub(pattern, r'<code>\1</code>', markdown)

## Tests

assert parse_inline_code("Use `let` to declare the variable.") == "Use <code>let</code> to declare the variable."
assert parse_inline_code("Use `let` or `const` to declare a variable.") == "Use <code>let</code> or <code>const</code> to declare a variable."
assert parse_inline_code("Run `npm install` then `npm start`.") == "Run <code>npm install</code> then <code>npm start</code>."