# Problem Description
#
# Given an array A of length N, your task is to
# find the maximum possible sum of any non-empty contiguous subarray.
#
# In other words, among all possible subarrays of A,
# determine the one that yields the highest sum and return that sum.
# Problem Constraints
#
# 1 <= N <= 106
# -1000 <= A[i] <= 1000
#
# Input Format
# The first and the only argument contains an integer array, A.
#
# Output Format
# Return an integer representing the maximum possible sum of the contiguous subarray.

# We can use Carry Forward or Prefix Sum to find the max sum - O(n^2) approach for now
# Later using Kadane we can bring it down to O(n)
# Brute Force is O(n^3)

def solve(A):
    n = len(A)
    max_sum = -1000
    pf_sum = [A[0]]
    # sum_val = 0

    for i in range(n):
        pf_sum.append(A[i] + pf_sum[i - 1])

    for i in range(0, n):
        sum_val = 0
        for j in range(i, n):
            sum_val += A[j]
            max_sum = max(max_sum, sum_val)
            # if j == 0:
            #     sum_val = pf_sum[j]
            # else:
            #     sum_val = pf_sum[j] - pf_sum[i - 1]

        # max_sum = max(sum_val, max_sum)

    return max_sum


res = solve([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(res)
