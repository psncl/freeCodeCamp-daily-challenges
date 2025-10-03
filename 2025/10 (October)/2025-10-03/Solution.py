def check_strength(password):

    def upper_and_lower(string):
        return any(ch.isalpha() for ch in string) and string != string.upper() and string != string.lower()

    SPECIAL_CHARS = "!@#$%^&*"

    flags = {
        'is_eight_long': len(password) >= 8,
        'contains_upper_lower': upper_and_lower(password),
        'contains_one_number': any(ch.isdigit() for ch in password),
        'contains_special_char': any(ch in SPECIAL_CHARS for ch in password)
    }

    rules_met = sum(1 for value in flags.values() if value is True)

    match rules_met:
        case 4:
            return "strong"
        case 3 | 2:
            return "medium"
        case 1 | 0:
            return "weak"
