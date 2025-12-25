def generate_snowflake(crystals: str) -> str:

    lines = crystals.split("\n")
    mirrored = [f"{line}{line[::-1]}" for line in lines]
    return "\n".join(mirrored)

## Tests

assert generate_snowflake("* \n *\n* ") == "*  *\n ** \n*  *"
assert generate_snowflake("X=~") == "X=~~=X"
assert generate_snowflake(" X  \n  v \nX--=\n  ^ \n X  ") == " X    X \n  v  v  \nX--==--X\n  ^  ^  \n X    X "
assert generate_snowflake("*   *\n * * \n* * *\n * * \n*   *") == "*   **   *\n * *  * * \n* * ** * *\n * *  * * \n*   **   *"
assert generate_snowflake("*  -\n * -\n*  -") == "*  --  *\n * -- * \n*  --  *"