# Problem Description
# You are given an integer array A.
# You have to find the second largest element/value in the array or report that no such element exists
# Input Format
# The first argument is an integer array A.
#
#
#
# Output Format
# Return the second largest element. If no such element exist then return -1.
# A = 1 2 3 4 5 6 3 2
# max element = 6
# second max = 5
# A = -5 -4 -3 -2 -1 0 -3 -4
# A = -5 -4 -3 -2 -1 -3 -4

"""
Initial Approach
# def solve(A):
#     n = len(A)
#     max_val = -1
#
#     if n == 1:
#         return -1
#
#     # We find the max element
#     for i in range(0, n):
#         if A[i] > max_val:
#             max_val = A[i]
#
#     for i in range(0, n):
#         A[i] -= max_val
#
#
#     second_max_val = -1000000000
#     for i in range(0, len(A)):
#         if second_max_val < A[i] != 0:
#             second_max_val = A[i]
#
#     if second_max_val + max_val == max_val or second_max_val == -1000000000:
#         return -1
#
#     return second_max_val + max_val
"""


def solve(A):
    max_elem = -1
    for x in A:
        if x > max_elem:
            max_elem = x

    second_max = -1
    for x in A:
        if x > second_max and x != max_elem:
            second_max = x
    return second_max


res = solve([20, 12, 15, 19, 13, 5, 13, 12, 18])
print(res)