def spookify(boo: str) -> str:

    replaced = ""
    capitalize_index = 0

    for i, ch in enumerate(boo):
        if ch == "-" or ch == "_":
            replaced += "~"
            capitalize_index += 1
        elif i == capitalize_index:
            replaced += ch.upper()
            capitalize_index += 2
        else:
            replaced += ch.lower()

    return replaced

## Tests

assert spookify("hello_world") == "HeLlO~wOrLd"
assert spookify("Spooky_Case") == "SpOoKy~CaSe"
assert spookify("TRICK-or-TREAT") == "TrIcK~oR~tReAt"
assert spookify("c_a-n_d-y_-b-o_w_l") == "C~a~N~d~Y~~b~O~w~L"
assert spookify("thE_hAUntEd-hOUsE-Is-fUll_Of_ghOsts") == "ThE~hAuNtEd~HoUsE~iS~fUlL~oF~gHoStS"