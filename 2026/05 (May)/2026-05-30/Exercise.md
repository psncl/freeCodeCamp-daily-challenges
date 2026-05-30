# Best Hand

https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-30

Given an array of five strings representing playing cards, return the name of the best hand.

- Each card is represented as a two-character string: the rank followed by the suit, `"2h"` for example.
  - Ranks, from low to high, are: `"2"`, `"3"`, `"4"`, `"5"`, `"6"`, `"7"`, `"8"`, `"9"`, `"T"`, `"J"`, `"Q"`, `"K"`, and `"A"`.
  - Suits are: `"h"`, `"d"`, `"c"`, and `"s"`.
- Aces (`"A"`) can be used as high or low in a straight.

The hands, in order from worst to best, are:

| Name                | Description                                        |
| ------------------- | -------------------------------------------------- |
| `"High Card"`       | No pair or better                                  |
| `"Pair"`            | Two of one rank                                    |
| `"Two Pair"`        | Two of one rank and two of another                 |
| `"Three of a Kind"` | Three of one rank                                  |
| `"Straight"`        | Five ranks in a row                                |
| `"Flush"`           | Five of the same suit                              |
| `"Full House"`      | Three of one rank, and two of another              |
| `"Four of a Kind"`  | Four of one rank                                   |
| `"Straight Flush"`  | Five ranks in a row of the same suit               |
| `"Royal Flush"`     | `"A"`, `"K"`, `"Q"`, `"J"`, `"T"` of the same suit |

Return the name of the best hand.

## Tests

1. `get_best_hand(["7s", "7h", "7d", "2c", "5h"])` should return `"Three of a Kind"`.
1. `get_best_hand(["Ks", "Kh", "Kd", "4s", "4h"])` should return `"Full House"`.
1. `get_best_hand(["2h", "5h", "7h", "9h", "Jh"])` should return `"Flush"`.
1. `get_best_hand(["As", "Ah", "Ad", "Ac", "Kh"])` should return `"Four of a Kind"`.
1. `get_best_hand(["Ts", "Th", "9d", "9c", "8h"])` should return `"Two Pair"`.
1. `get_best_hand(["9c", "8c", "7c", "6c", "5c"])` should return `"Straight Flush"`.
1. `get_best_hand(["As", "Kh", "Jd", "8c", "5h"])` should return `"High Card"`.
1. `get_best_hand(["As", "2h", "3d", "4c", "5h"])` should return `"Straight"`.
1. `get_best_hand(["Ts", "Th", "7c", "6d", "5h"])` should return `"Pair"`.
1. `get_best_hand(["As", "Ks", "Qs", "Js", "Ts"])` should return `"Royal Flush"`.
