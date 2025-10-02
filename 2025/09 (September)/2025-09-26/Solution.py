def speeding(speeds, limit):
    overs = [(speed - limit) for speed in speeds if speed > limit]
    return [len(overs), sum(overs) / len(overs)] if len(overs) > 0 else [0, 0]