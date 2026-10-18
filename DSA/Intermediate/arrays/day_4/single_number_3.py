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
    for x in A:
        xor ^= x

    print(xor)




res = solve([1, 2, 3, 1, 2, 4])
print(res)