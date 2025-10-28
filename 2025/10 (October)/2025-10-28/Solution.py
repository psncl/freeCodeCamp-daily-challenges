def navigate(commands: list[str]) -> str:

    pages = ["Home"]
    currentPage = 1

    for command in commands:
        if command.startswith("Visit "):
            pages = pages[:currentPage]
            pages.append(command.replace("Visit ", "", 1))
            currentPage = len(pages)
        elif command == "Back":
            if currentPage > 1:
                currentPage -= 1
        elif command == "Forward":
            if currentPage < len(pages):
                currentPage += 1

    return pages[currentPage - 1]

## Tests

assert navigate(["Visit About Us", "Back", "Forward"]) == "About Us"
assert navigate(["Forward"]) == "Home"
assert navigate(["Back"]) == "Home"
assert navigate(["Visit About Us", "Visit Gallery"]) == "Gallery"
assert navigate(["Visit About Us", "Visit Gallery", "Back", "Back"]) == "Home"
assert navigate(["Visit About", "Visit Gallery", "Back", "Visit Contact", "Forward"]) == "Contact"
assert navigate(["Visit About Us", "Visit Visit Us", "Forward", "Visit Contact Us", "Back"]) == "Visit Us"