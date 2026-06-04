from typing import Any

VALID_ROLES: frozenset[str] = frozenset({
    "user",
    "creator",
    "moderator",
    "staff",
    "admin"
})

def is_valid_schema(obj: dict[str, Any]) -> bool:

    try:
        validity = (
            isinstance(obj["username"], str)
            and is_strict_int(obj["posts"])
            and isinstance(obj["verified"], bool)
            and obj["role"] in VALID_ROLES
        )
        
        if "supporter" in obj:
            validity = validity and isinstance(obj["supporter"], bool)
        
        return validity
    except KeyError:
        return False

def is_strict_int(val: Any) -> bool:
        """int check that excludes bool (bool is a subclass of int in Python)."""
        return isinstance(val, int) and not isinstance(val, bool)

## Tests

assert is_valid_schema({"username": "vivian", "posts": 1, "verified": False, "role": "user", "supporter": True}) == True
assert is_valid_schema({"username": "rudolph", "posts": 15, "verified": True, "role": "creator"}) == True
assert is_valid_schema({"username": "hernandez", "posts": 35, "verified": True, "role": "moderator", "supporter": False, "followers": 55}) == True
assert is_valid_schema({"username": "julia", "posts": 50, "verified": True, "role": "admin", "supporter": "true"}) == False
assert is_valid_schema({"username": "bernard", "posts": 0, "verified": True, "role": "friend", "supporter": True}) == False
assert is_valid_schema({"username": "felix", "posts": 40, "verified": "yes", "role": "staff", "supporter": False}) == False
assert is_valid_schema({"username": "jimmy", "posts": True, "verified": False, "role": "creator", "supporter": True}) == False
assert is_valid_schema({"username": True, "posts": 30, "verified": True, "role": "moderator", "supporter": False}) == False