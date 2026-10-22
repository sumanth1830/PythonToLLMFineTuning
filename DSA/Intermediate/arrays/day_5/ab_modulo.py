# Problem Description
# Given two integers A and B, find the greatest possible positive integer M,
# such that A % M = B % M.
# Input Format
# The first argument is an integer A.
# The second argument is an integer B.
# Output Format
# Return an integer denoting the greatest possible positive M.
# A = 1
# B = 2
# 1

def solve(A, B):
    return abs(A - B)


res = solve(5, 10)
print(res)