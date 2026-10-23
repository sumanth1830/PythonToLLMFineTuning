# Problem Description
# You are given an integer array A of size N.
# You have to perform B operations. In one operation,
# you can remove either the leftmost or the rightmost element of the array A.
# Find and return the maximum possible sum of the B elements that were removed after the B operations.
# NOTE: Suppose B = 3, and array A contains 10 elements, then you can:
#
#     Remove 3 elements from front and 0 elements from the back, OR
#     Remove 2 elements from front and 1 element from the back, OR
#     Remove 1 element from front and 2 elements from the back, OR
#     Remove 0 elements from front and 3 elements from the back
#
# Problem Constraints
# 1 <= N <= 105
# 1 <= B <= N
# -103 <= A[i] <= 103
#
# Input Format
# First argument is an integer array A.
# Second argument is an integer B.
#
# Output Format
# Return an integer denoting the maximum possible sum of elements you removed.
# A = [5, -2, 3 , 1, 2]
# B = 3
# O/P:  8

# How to do this in O(1) Space complexity
# We surely need two arrays/lists to store the suffix and prefix sum
# We can store both as a tuple in the same list alongside the given Array values

# Brute Force Logic
# Loop over B elements: i elements from left + n - B + i elements from right
# for i in range(B + 1):
#     current_sum = 0
#     # Sum first i elements
#     for j in range(i):
#         current_sum += A[j]
#     # Sum last (B-i) elements
#     for j in range(n - (B - i), n):
#         current_sum += A[j]
#     max_sum = max(max_sum, current_sum)

def solve(A, B):
    if B == 1:
        return max(A[0], A[-1])

    n = len(A)
    current_sum = sum(A[:B])
    max_sum = current_sum

    for i in range(1, B + 1):
        current_sum = current_sum - A[B - i] + A[n - i]
        max_sum = max(max_sum, current_sum)

    return max_sum


# res = solve([5, -2, 3 , 1, 2], 4)
# res = solve([2, 2, 2, 3, 1, -5, 2, 2, 2], 5)
res = solve(
    [-533,-666,-500,169,724,478,358,-38,-536,705,-855,281,-173,961,-509,-5,942,-173,436,-609,-396,902,-847,-708,-618,421,-284,718,895,447,726,-229,538,869,912,667,-701,35,894,-297,811,322,-667,673,-336,141,711,-747,-132,547,644,-338,-243,-963,-141,-277,741,529,-222,-684,35],
    48
)
print(res)


# Approach 1 : TC and SC are of O(n)
#     if B == 1:
#         return max(A[0], A[-1])
#
#     n = len(A)
#     pf_left_sum = [A[0]]
#     pf_right_sum = [0] * n
#     pf_right_sum[n - 1] = A[n - 1]
#     for i in range(1, n):
#         pf_left_sum.append(A[i] + pf_left_sum[i - 1])
#
#     for i in range(n-2, -1, -1):
#         pf_right_sum[i] = A[i] + pf_right_sum[i + 1]
#
#     # print(pf_right_sum)
#     # print(pf_left_sum)
#     # print(f"Length : {n}")
#     max_sum = max(pf_left_sum[B - 1], pf_right_sum[n - B])
#
#     for i in range(1, B):
#         val = pf_left_sum[i - 1] + pf_right_sum[n - B + i]
#         max_sum = max(max_sum, val)
#
#     return max_sum


# Approach 2: SC -> O(1)
# if B == 1:
#     return max(A[0], A[-1])
#
# n = len(A)
# max_sum = max(sum(A[:B]), sum(A[n-B:]))
# left_sum = 0
# right_sum = sum(A[n - B:])
# for i in range(0, B):
#     left_sum += A[i]
#     right_sum -= A[n - B + i]
#     val = left_sum + right_sum
#     max_sum = max(max_sum, val)
#
# return max_sum