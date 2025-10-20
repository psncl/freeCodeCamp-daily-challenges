def calculate_tips(meal_price: str, custom_tip: str) -> list[str]:

    price = float(meal_price[1:])
    custom_tip_multiplier = int(custom_tip[:-1]) / 100
    multipliers: list[float] = [15/100, 20/100, custom_tip_multiplier]

    def amt_to_string(amount: float) -> str:
        return f"${amount:.2f}"

    return [amt_to_string(price * multiplier) for multiplier in multipliers]

## Tests

assert calculate_tips("$10.00", "25%") == ["$1.50", "$2.00", "$2.50"]
assert calculate_tips("$89.67", "26%") == ["$13.45", "$17.93", "$23.31"]
assert calculate_tips("$19.85", "9%") == ["$2.98", "$3.97", "$1.79"]