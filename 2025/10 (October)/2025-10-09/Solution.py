from datetime import date, datetime

def moon_phase(date_string: str) -> str:

    CYCLE_LENGTH = 28
    REFERENCE_DATE = date(2000, 1, 6)
    moon_phases = [
        (22, "Waning"),
        (15, "Full"),
        (8, "Waxing"),
        (1, "New"),
    ]

    cur_date = parse_date(date_string)
    difference_days_total = (cur_date - REFERENCE_DATE).days + 1
    difference_days_cycle = difference_days_total % CYCLE_LENGTH
    
    for (days, phase) in moon_phases:
        if difference_days_cycle >= days:
            return phase
    
def parse_date(input_str: str) -> date:
    date_format = "%Y-%m-%d"
    return datetime.strptime(input_str, date_format).date()

## Tests

assert moon_phase("2000-01-12") == "New"
assert moon_phase("2000-01-13") == "Waxing"
assert moon_phase("2014-10-15") == "Full"
assert moon_phase("2012-10-21") == "Waning"
assert moon_phase("2022-12-14") == "New"