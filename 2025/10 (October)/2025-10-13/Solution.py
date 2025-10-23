def to_12(time: str) -> str:

    hours = int(time[0:2])
    minutes = time[2:4]

    if hours > 12:
        return f"{hours - 12}:{minutes} PM"
    elif hours == 0:
        return f"{abs(hours - 12)}:{minutes} AM"
    else:
        return f"{hours}:{minutes} AM"

## Tests

assert to_12("1124") == "11:24 AM"
assert to_12("0900") == "9:00 AM"
assert to_12("1455") == "2:55 PM"
assert to_12("2346") == "11:46 PM"
assert to_12("0030") == "12:30 AM"