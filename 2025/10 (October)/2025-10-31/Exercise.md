# SpOoKy~CaSe

https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-31

Given a string representing a variable name, convert it to "spooky case" using the following constraints:

- Replace all underscores (`_`), and hyphens (`-`) with a tilde (`~`).
- Capitalize the first letter of the string, and every other letter after that, ignore the tilde character when counting.

For example, given `hello_world`, return `HeLlO~wOrLd`.

## Tests

1. `spookify("hello_world")` should return`"HeLlO~wOrLd"`.
1. `spookify("Spooky_Case")` should return `"SpOoKy~CaSe"`.
1. `spookify("TRICK-or-TREAT")` should return `"TrIcK~oR~tReAt"`.
1. `spookify("c_a-n_d-y_-b-o_w_l")` should return `"C~a~N~d~Y~~b~O~w~L"`.
1. `spookify("thE_hAUntEd-hOUsE-Is-fUll_Of_ghOsts")` should return `"ThE~hAuNtEd~HoUsE~iS~fUlL~oF~gHoStS"`.
