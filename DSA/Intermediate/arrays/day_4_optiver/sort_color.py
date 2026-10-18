# Given an array with N objects colored red, white, or blue,
# sort them so that objects of the same color are adjacent,
# with the colors in the order red, white, and blue.
#
# We will represent the colors as,
#
# red -> 0
# white -> 1
# blue -> 2
#
# Note: Using the library sort function is not allowed.
# Input Format
# First and only argument of input contains an integer array A.
# Output Format
# Return an integer array in asked order

def solve(A):
    A.sort()
    return A





res = solve([0, 1, 2, 0, 1, 2])
print(res)