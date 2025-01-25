#rain

Edge Case: Return 0 if the list is empty or has fewer than 3 walls—no water can be retained.

Left and Right Max Arrays:

left_max[i] holds the tallest wall from the start to index i.
right_max[i] holds the tallest wall from index i to the end.

For the Water Calculation:

For each wall, water retained = min(left_max[i], right_max[i]) - walls[i]. Add this for all walls.

Result: Sum the retained water for all valid indices.

Example:
Input: [0, 1, 0, 2, 0, 3, 0, 4]
Output: 6.