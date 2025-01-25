#!/usr/bin/python3
"""
Calculate rainwater retention given wall heights.
"""

def rain(walls):
    """
    Calculate how many square units of water will be retained after it rains.

    :param walls: List of non-negative integers representing wall heights
    :return: Integer indicating total amount of rainwater retained
    """
    if not walls or len(walls) < 3:
        return 0

    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n
    water_retained = 0

    # Fill left_max array
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    # Fill right_max array
    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    # Calculate the water retained
    for i in range(1, n - 1):
        water_retained += max(0, min(left_max[i], right_max[i]) - walls[i])

    return water_retained