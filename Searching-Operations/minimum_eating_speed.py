def can_finish(piles, h, speed):
    hours = 0
    for pile in piles:
        # Integer math trick for ceiling division
        hours += (pile + speed - 1) // speed
    return hours <= h