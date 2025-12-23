def get_amount_in_usd(item: list[str])-> float:
    """
    Parse an item in the format ["10.00", "EUR"] and convert it into equivalent USD amount.
    """

    CURRENCIES_TO_USD: dict[str, float] = {
        'USD': 1.0,
        'EUR': 1.1,
        'GBP': 1.25,
        'JPY': 0.007,
        'CAD': 0.75
    }

    return float(item[0]) * CURRENCIES_TO_USD[item[1]]

def buy_items(funds: list[str], items: list[list[str]]) ->str:

    money_available_in_usd = get_amount_in_usd(funds)

    can_afford = 0

    for item in items:
        cost_current_item = get_amount_in_usd(item)

        # Reached limit of items you can afford
        if cost_current_item > money_available_in_usd:
            break
        
        can_afford += 1
        money_available_in_usd -= cost_current_item

    if can_afford == len(items):
        return "Buy them all!"
    else:
        return f"Buy the first {can_afford} items."

## Tests

assert buy_items(["150.00", "USD"], [["50.00", "USD"], ["75.00", "USD"], ["30.00", "USD"]]) == "Buy the first 2 items."
assert buy_items(["200.00", "EUR"], [["50.00", "USD"], ["50.00", "USD"]]) == "Buy them all!"
assert buy_items(["100.00", "CAD"], [["20.00", "USD"], ["15.00", "EUR"], ["10.00", "GBP"], ["6000", "JPY"], ["5.00", "CAD"], ["10.00", "USD"]]) == "Buy the first 3 items."
assert buy_items(["5000", "JPY"], [["3.00", "USD"], ["1000", "JPY"], ["5.00", "CAD"], ["2.00", "EUR"], ["4.00", "USD"], ["2000", "JPY"]]) == "Buy them all!"
assert buy_items(["200.00", "USD"], [["50.00", "USD"], ["40.00", "EUR"], ["30.00", "GBP"], ["5000", "JPY"], ["25.00", "CAD"], ["20.00", "USD"]]) == "Buy the first 5 items."