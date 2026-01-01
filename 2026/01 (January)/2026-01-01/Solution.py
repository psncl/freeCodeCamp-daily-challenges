def resolution_streak(days: list[list[int]]) -> str:

    successful_days = 0

    for day in days:
        if not is_day_successful(day):
            break
        
        successful_days += 1
    
    if successful_days == len(days):
        return f"Resolution on track: {successful_days} day streak."
    else:
        return f"Resolution failed on day {successful_days + 1}: {successful_days} day streak."

def is_day_successful(day_activities: list[int]) -> bool:

    min_steps = 10000
    max_screen_time = 120
    min_pages_read = 5

    return day_activities[0] >= min_steps and day_activities[1] <= max_screen_time and day_activities[2] >= min_pages_read

## Tests

assert resolution_streak([[10500, 75, 15], [11000, 90, 10], [10650, 100, 9]]) == "Resolution on track: 3 day streak."
assert resolution_streak([[10000, 120, 5], [10950, 121, 11]]) == "Resolution failed on day 2: 1 day streak."
assert resolution_streak([[15000, 110, 8], [12300, 60, 13], [10100, 120, 4], [9000, 125, 4]]) == "Resolution failed on day 3: 2 day streak."
assert resolution_streak([[11600, 76, 13], [12556, 64, 26], [10404, 32, 59], [9999, 44, 124], [7508, 23, 167], [10900, 80, 0]]) == "Resolution failed on day 4: 3 day streak."
assert resolution_streak([[10500, 75, 15], [11000, 90, 10], [10650, 100, 9], [10200, 60, 10], [10678, 87, 9], [12431, 67, 13], [10444, 107, 19], [10111, 95, 5], [10000, 120, 7], [11980, 101, 8]]) == "Resolution on track: 10 day streak."