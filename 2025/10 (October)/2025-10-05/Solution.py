def has_exoplanet(readings: str) -> bool:

    luminosities = [luminosity_value(reading) for reading in readings]
    avg_readings = sum(luminosities) / len(luminosities)
    
    return any(luminosity <= (0.8 * avg_readings) for luminosity in luminosities)

def luminosity_value(reading: str) -> int:
    return get_luminosity_table()[reading]

def get_luminosity_table() -> dict[str, int]:
    """
    Construct a dictionary of luminosity values,
    mapping '0'-'9' to 0-9 and 'A'-'Z' to 10-35.
    """

    luminosity_table: dict[str, int] = {}

    def get_next_luminosity_level(luminosity_dict: dict[str, int]) -> int:
        last_key = list(luminosity_dict.keys())[-1]
        return luminosity_dict[last_key] + 1

    # Assign {'0': 0}, {'1': 1} and so on...
    for num in range(0, 10):
        luminosity_table[f"{num}"] = num

    # 'A' to 'Z' correspond to ASCII codes from 65 to 90,
    # resulting in an offset of 55 from 10 to 35.
    offset = ord('A') - get_next_luminosity_level(luminosity_table)

    for letter in range(ord('A'), ord('Z') + 1):
        luminosity_table[chr(letter)] = letter - offset
    
    return luminosity_table

## TESTS

assert has_exoplanet("665544554") == False
assert has_exoplanet("FGFFCFFGG") == True
assert has_exoplanet("MONOPLONOMONPLNOMPNOMP") == False
assert has_exoplanet("FREECODECAMP") == True
assert has_exoplanet("9AB98AB9BC98A") == False
assert has_exoplanet("ZXXWYZXYWYXZEGZXWYZXYGEE") == True