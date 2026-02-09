from typing import Literal

def ski_jump_medal(distance_points: float, style_points: float, wind_comp: float, k_point_bonus: float) -> Literal["Gold", "Silver", "Bronze", "No Medal"]:

    existing_scores: list[float] = [
        165.5,
        172.0,
        158.0,
        180.0,
        169.5,
        175.0,
        162.0,
        170.0
    ]

    current_score = distance_points + style_points + wind_comp + k_point_bonus
    existing_scores.append(current_score)
    top_scores = sorted(existing_scores, reverse=True)[0:3]

    # The following logic assumes that no two scores are equal
    if current_score == top_scores[0]:
        return "Gold"
    elif current_score == top_scores[1]:
        return "Silver"
    elif current_score == top_scores[2]:
        return "Bronze"
    else:
        return "No Medal"

## Tests

assert ski_jump_medal(125.0, 58.0, 0.0, 6.0) == "Gold"
assert ski_jump_medal(119.0, 50.0, 1.0, 4.0) == "Bronze"
assert ski_jump_medal(122.0, 52.0, -1.0, 4.0) == "Silver"
assert ski_jump_medal(118.0, 50.5, -1.5, 4.0) == "No Medal"
assert ski_jump_medal(124.0, 50.5, 2.0, 5.0) == "Gold"
assert ski_jump_medal(119.0, 49.5, 0.0, 3.0) == "No Medal"
