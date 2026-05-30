# NOTE: Most of this solution was written by Claude.
# I am learning how to direct agents to solve a problem.
# I did refactor a few code inconsistencies to match my own coding style in Python.

from collections import Counter
from typing import Callable, NamedTuple

## Define types

class HandFeatures(NamedTuple):
    nums: list[int]
    flush: bool
    straight: bool
    counts: Counter[str]

Predicate = Callable[[HandFeatures], bool]

## Business logic

def parse(cards: list[str]) -> tuple[list[str], list[str]]:
    ranks = [c[0] for c in cards]
    suits = [c[1] for c in cards]
    return ranks, suits

def features(ranks: list[str], suits: list[str]) -> HandFeatures:
    RANK_ORDER = "23456789TJQKA"

    nums = sorted(RANK_ORDER.index(r) for r in ranks)
    is_flush = len(set(suits)) == 1
    is_straight = (nums == list(range(nums[0], nums[0] + 5))
                   or nums == [0, 1, 2, 3, 12])  # ace-low: A-2-3-4-5
    counts = Counter(ranks)
    
    return HandFeatures(nums, is_flush, is_straight, counts)


def is_royal_flush(f: HandFeatures) -> bool:
    return f.flush and set(f.nums) == {8, 9, 10, 11, 12}


def is_straight_flush(f: HandFeatures) -> bool:
    return f.flush and f.straight


def is_four_of_a_kind(f: HandFeatures) -> bool:
    return 4 in f.counts.values()


def is_full_house(f: HandFeatures) -> bool:
    return sorted(f.counts.values()) == [2, 3]


def is_flush_hand(f: HandFeatures) -> bool:
    return f.flush


def is_straight_hand(f: HandFeatures) -> bool:
    return f.straight


def is_three_of_a_kind(f: HandFeatures) -> bool:
    return 3 in f.counts.values()


def is_two_pair(f: HandFeatures) -> bool:
    return list(f.counts.values()).count(2) == 2


def is_pair(f: HandFeatures) -> bool:
    return 2 in f.counts.values()


def is_high_card(f: HandFeatures) -> bool:
    return True


HANDS: list[tuple[str, Predicate]] = [
    ("Royal Flush",     is_royal_flush),
    ("Straight Flush",  is_straight_flush),
    ("Four of a Kind",  is_four_of_a_kind),
    ("Full House",      is_full_house),
    ("Flush",           is_flush_hand),
    ("Straight",        is_straight_hand),
    ("Three of a Kind", is_three_of_a_kind),
    ("Two Pair",        is_two_pair),
    ("Pair",            is_pair),
    ("High Card",       is_high_card),
]


def get_best_hand(cards: list[str]) -> str:
    ranks, suits = parse(cards)
    feats = features(ranks, suits)
    for name, predicate in HANDS:
        if predicate(feats):
            return name

## Tests

assert get_best_hand(["7s", "7h", "7d", "2c", "5h"]) == "Three of a Kind"
assert get_best_hand(["Ks", "Kh", "Kd", "4s", "4h"]) == "Full House"
assert get_best_hand(["2h", "5h", "7h", "9h", "Jh"]) == "Flush"
assert get_best_hand(["As", "Ah", "Ad", "Ac", "Kh"]) == "Four of a Kind"
assert get_best_hand(["Ts", "Th", "9d", "9c", "8h"]) == "Two Pair"
assert get_best_hand(["9c", "8c", "7c", "6c", "5c"]) == "Straight Flush"
assert get_best_hand(["As", "Kh", "Jd", "8c", "5h"]) == "High Card"
assert get_best_hand(["As", "2h", "3d", "4c", "5h"]) == "Straight"
assert get_best_hand(["Ts", "Th", "7c", "6d", "5h"]) == "Pair"
assert get_best_hand(["As", "Ks", "Qs", "Js", "Ts"]) == "Royal Flush"