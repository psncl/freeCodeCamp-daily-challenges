def get_fastest_speed(times: list[float]) -> str:

    length_segments: list[int] = [320, 280, 350, 300, 250]

    speed_segments = [length / time for length, time in zip(length_segments, times)]
    max_speed = max(speed_segments)

    return f"The luger's fastest speed was {max_speed:.02f} m/s on segment {speed_segments.index(max_speed) + 1}."

## Tests

assert get_fastest_speed([9.523, 8.234, 10.012, 9.001, 7.128]) == "The luger's fastest speed was 35.07 m/s on segment 5."
assert get_fastest_speed([9.381, 7.417, 9.912, 8.815, 7.284]) == "The luger's fastest speed was 37.75 m/s on segment 2."
assert get_fastest_speed([8.890, 7.601, 9.093, 8.392, 6.912]) == "The luger's fastest speed was 38.49 m/s on segment 3."
assert get_fastest_speed([8.490, 7.732, 10.103, 8.489, 6.840]) == "The luger's fastest speed was 37.69 m/s on segment 1."
assert get_fastest_speed([8.204, 7.230, 9.673, 7.645, 6.508]) == "The luger's fastest speed was 39.24 m/s on segment 4."