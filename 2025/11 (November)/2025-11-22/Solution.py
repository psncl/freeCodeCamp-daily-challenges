def scale_recipe(ingredients: list[str], scale: float) -> list[str]:

    def scale_ingredient(ing: str) -> str:
        quantity_str, rest = ing.split(" ", maxsplit=1)
        scaled_quantity = float(quantity_str) * scale
        scaled_quantity_truncated = int(scaled_quantity) if scaled_quantity.is_integer() else scaled_quantity
        return f"{scaled_quantity_truncated} {rest}"
    
    return [scale_ingredient(ingredient) for ingredient in ingredients]

## Tests

assert scale_recipe(["2 C Flour", "1.5 T Sugar"], 2) == ["4 C Flour", "3 T Sugar"]
assert scale_recipe(["4 T Flour", "1 C Milk", "2 T Oil"], 1.5) == ["6 T Flour", "1.5 C Milk", "3 T Oil"]
assert scale_recipe(["3 C Milk", "2 C Oats"], 0.5) == ["1.5 C Milk", "1 C Oats"]
assert scale_recipe(["2 C All-purpose Flour", "1 t Baking Soda", "1 t Salt", "1 C Butter", 
                    "0.5 C Sugar", "0.5 C Brown Sugar", "1 t Vanilla Extract", "2 C Chocolate Chips"], 2.5) \
                     == ["5 C All-purpose Flour", "2.5 t Baking Soda", "2.5 t Salt", "2.5 C Butter", "1.25 C Sugar", 
                     "1.25 C Brown Sugar", "2.5 t Vanilla Extract", "5 C Chocolate Chips"]