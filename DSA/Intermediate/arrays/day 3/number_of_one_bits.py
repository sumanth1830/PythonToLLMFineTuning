# Problem Description
# Write a function that takes an integer and
# returns the number of 1 bits present in its binary representation.
# Input Format
# First and only argument contains integer A
# Output Format
# Return an integer
# 11
# 3

def solve(A):
    ret = 0
    while A != 0:
        # rightmost set bit becomes unset
        A = A & (A - 1)
        ret += 1

    return ret


res = solve(6)
print(res)