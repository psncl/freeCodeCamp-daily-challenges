from datetime import datetime, date

def calculate_age(birthday: str) -> int:

    DAYS_IN_A_YEAR = 365.25
    REFERENCE_DATE = date(2025, 11, 27)
    birth_date = parse_date(birthday)

    difference_days = (REFERENCE_DATE - birth_date).days + 1
    return int(difference_days / DAYS_IN_A_YEAR)

def parse_date(input_str: str) -> date:
    date_format = "%Y-%m-%d"
    return datetime.strptime(input_str, date_format).date()

## Tests

assert calculate_age("2000-11-20") == 25
assert calculate_age("2000-12-01") == 24
assert calculate_age("2014-10-25") == 11
assert calculate_age("1994-01-06") == 31
assert calculate_age("1994-12-14") == 30