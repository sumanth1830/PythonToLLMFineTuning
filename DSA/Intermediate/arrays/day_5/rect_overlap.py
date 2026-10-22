# Eight integers A, B, C, D, E, F, G, and H represent two rectangles in a 2D plane.
# For the First rectangle,
#
#     Bottom left corner is (A, B)
#     Top right corner is (C, D)
#
# For the Second rectangle,
#
#     Bottom left corner is (E, F)
#     Top right corner is (G, H).
#
# Find and return whether the two rectangles overlap or not.
# Input Format
# The eight arguments are integers A, B, C, D, E, F, G, and H.
# Output Format
# Return 1 if the two rectangles overlap else, return 0.
# A = 0   B = 0
# C = 4   D = 4
# E = 2   F = 2
# G = 6   H = 6
# 1

def solve(A, B, C, D, E, F, G, H):
    if C <= E or A >= G:
        return 0
    if D <= F or B >= H:
        return 0

    return 1


res = solve(0, 0, 4, 4, 2, 2, 6, 6)
print(res)