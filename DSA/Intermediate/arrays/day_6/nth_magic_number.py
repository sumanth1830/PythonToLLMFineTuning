# Problem Description
# Given an integer A, find and return the Ath magic number.
# A magic number is defined as a number that can be expressed as a power of 5
# or a sum of unique powers of 5.
# First few magic numbers are 5, 25, 30(5 + 25), 125, 130(125 + 5), ….
# Problem Constraints
# 1 <= A <= 5000
# Input Format
# The only argument given is integer A.
# Output Format
# Return the Ath magic number.

def solve(A):
    ans = 0
    x = 1
    while A > 0:
        x *= 5
        if A % 2 == 1:
            ans += x

        A = A // 2

    return ans



res = solve(15)
print(res)