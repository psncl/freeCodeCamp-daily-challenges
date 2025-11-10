def get_extension(filename: str) -> str:

    period_loc = filename.rfind('.')

    if period_loc == -1 or period_loc == len(filename) - 1:
        return "none"

    return filename[period_loc + 1:]

## Tests

assert get_extension("document.txt") == "txt"
assert get_extension("README") == "none"
assert get_extension("image.PNG") == "PNG"
assert get_extension(".gitignore") == "gitignore"
assert get_extension("archive.tar.gz") == "gz"
assert get_extension("final.draft.") == "none"