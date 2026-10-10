# Problem Description
# Given an array A, find the size of the smallest subarray such that it contains at
# least one occurrence of the maximum value of the array
# and at least one occurrence of the minimum value of the array.
# Problem Constraints
# 1 <= |A| <= 2000
#
# Input Format
# First and only argument is vector A
#
# Output Format
# Return the length of the smallest subarray which has at least one occurrence of minimum and
# maximum element of the array
# A = [2, 6, 1, 6, 9]
# 3

def solve(A):
    n = len(A)
    min_index = 2001
    max_index = 2001
    min_len = n
    min_val = min(A)
    max_val = max(A)
    if max_val == min_val:
        return 1

    for i in range(n-1, -1, -1):
        # We can also traverse from left to right
        if A[i] == min_val:
            min_index = i

        if A[i] == max_val:
            max_index = i

        if max_index != 2001 and min_index != 2001:
            min_len = min(min_len, abs(min_index - max_index) + 1)

    return min_len


res = solve([2, 6, 1, 6, 9])
print(res)


# Brute force would be looping over twice blindly and then computing length
# On observing that subarray starts/ends with min/max
# The below approach comes into picture
# O(n) approach without carry forward
# def solve(A):
#     n = len(A)
#     min_index = 2001
#     max_index = 2001
#     min_len = n
#     min_val = min(A)
#     max_val = max(A)
#     if max_val == min_val:
#         return 1
#
#     for i in range(n):
#         if A[i] == min_val:
#             min_index = i
#             for j in range(i, n):
#                 if A[j] == min_val:
#                     min_index = i
#                 if A[j] == max_val:
#                     min_len = min(min_len, j - min_index + 1)
#
#         elif A[i] == max_val:
#             max_index = i
#             for j in range(i, n):
#                 if A[j] == max_val:
#                     max_index = i
#                 if A[j] == min_val:
#                     min_len = min(min_len, j - max_index + 1)
#
#
#     return min_len
