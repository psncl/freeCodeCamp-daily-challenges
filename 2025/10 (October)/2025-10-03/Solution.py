def check_strength(password):

    flags = {
        'is_eight_long': False,
        'contains_upper_lower': False,
        'contains_one_number': False,
        'contains_special_char': False
    }
    SPECIAL_CHARS = "!@#$%^&*"

    flags['is_eight_long'] = len(password) >= 8

    flags['contains_upper_lower'] = any(ch.isalpha() for ch in password) and password != password.upper() and password != password.lower()

    flags['contains_one_number'] = any(ch.isdigit() for ch in password)

    flags['contains_special_char'] = any(ch in SPECIAL_CHARS for ch in password)

    rules_met = sum(1 for value in flags.values() if value is True)

    match rules_met:
        case 4:
            return "strong"
        case 3 | 2:
            return "medium"
        case 1 | 0:
            return "weak"