from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

def get_oldest(people: list[Person]):

    oldest_age = max(people, key=lambda person: person["age"])["age"]
    return [person["name"] for person in people if person["age"] == oldest_age]

## Tests

assert get_oldest([{ "name": "Brenda", "age": 40 }]) == ["Brenda"]
assert get_oldest([{ "name": "Alice", "age": 30 }, { "name": "Bob", "age": 25 }]) == ["Alice"]
assert get_oldest([{ "name": "Allison", "age": 25 }, { "name": "Bill", "age": 30 }, { "name": "Carol", "age": 30 }]) == ["Bill", "Carol"]
assert get_oldest([{ "name": "George", "age": 50 }, { "name": "Shirley", "age": 42 }, { "name": "Beth", "age": 48 }, { "name": "Holly", "age": 50 }, { "name": "Kevin", "age": 44 }, { "name": "Frank", "age": 47 }, { "name": "Zach", "age": 50 }, { "name": "Jennifer", "age": 43 }]) == ["George", "Holly", "Zach"]