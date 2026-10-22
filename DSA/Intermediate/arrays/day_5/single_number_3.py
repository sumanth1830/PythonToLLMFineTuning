# Given an array of positive integers A, two integers appear only once,
# and all the other integers appear twice.
# Find the two integers that appear only once.
# Note: Return the two numbers in ascending order.
# Input Format
# The first argument is an array of integers of size N.
#
# Output Format
# Return an array of two integers that appear only once.
# A = [1, 2, 3, 1, 2, 4]
# [3, 4]

def solve(A):
    xor = 0
    grA = 0
    grB = 0
    # Result will have Xor value of two unique elements
    for x in A:
        xor ^= x

    # Now we create a mask to find the bit at which two elements differ
    # A & A - 1 gives the first bit at which elements differ - LSB will become 0 in A
    # (A & A - 1) ^ A gives the position of the LSB - mask
    mask = (xor & (xor - 1)) ^ xor
    
    # Are we
    for val in A:
        if val & mask:
            grA ^= val
        else:
            grB ^= val

    return [min(grA, grB), max(grA, grB)]


res = solve([1, 2, 3, 1, 2, 4])
print(res)