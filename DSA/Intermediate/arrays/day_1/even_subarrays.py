# Problem Description
# You are given an integer array A.
# Decide whether it is possible to divide the array into one or more subarrays of
# even length such that the first and last element of all subarrays will be even.
# Return "YES" if it is possible; otherwise, return "NO" (without quotes).
# Problem Constraints
# 1 <= |A|, A[i] <= 106
#
# Input Format
# The first and the only input argument is an integer array, A.
#
# Output Format
# Return a string "YES" or "NO" denoting the answer.
# A = [2, 4, 8, 7, 6]
# "NO"

def solve(A):
    n = len(A)

    # Obs
    # first and last has to be even
    # split into even length with above condition
    # divide the whole array into even length sub arrays

    # Means length of array should be even
    # Start and end should be even as well
    # To satisfy the conditions

    if n % 2 == 0 or A[0] % 2 == 1 or A[-1] % 2 == 1:
        return "NO"

    return "YES"


res = solve([2, 4, 8, 7, 6])
print(res)

# Another approach
# Looping over array and verifying if the array can be split at even numbers and even length
# def solve(self, A):
#     count = 1
#     if A[0] % 2 == 1 or A[-1] % 2 == 1:
#         return "NO"
#
#     for i in range(1, len(A)):
#         if A[i - 1] % 2 == 0 and A[i] % 2 == 0 and count % 2 == 0 and count != 0:
#             count = 1
#         else:
#             count += 1
#
#     if count % 2 == 0:
#         return "YES"
#
#     return "NO"