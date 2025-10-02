def cost_to_fill(tank_size, fuel_level, price_per_gallon):
    amount = (tank_size - fuel_level) * price_per_gallon
    str = '{:.2f}'.format(round(amount, 2))
    return f"${str}"