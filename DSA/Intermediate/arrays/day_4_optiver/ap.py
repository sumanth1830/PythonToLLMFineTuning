# Given an integer array A of size N.
# Return 1 if the array can be arranged to form an arithmetic progression, otherwise return 0.
#
# A sequence of numbers is called an arithmetic progression if the difference between
# any two consecutive elements is the same.
# Input Format
# The first and only argument is an integer array A of size N.
# Output Format
# Return 1 if the array can be rearranged to form an arithmetic progression, otherwise return 0.
# A = [3, 5, 1]
# O/P: 1

def solve(A):
    n = len(A)
    A.sort()
    a = A[0]
    d = A[1] - a

    for i in range(2, n):
        if A[i] - A[i - 1] != d:
            return 0

    return 1



res = solve([3, 5, 1])
print(res)