# Problem Description
# Given an array A of size N, find the subarray of size B with the least average.
# Problem Constraints
# 1 <= B <= N <= 105
# -105 <= A[i] <= 105
# Input Format
# First argument contains an array A of integers of size N.
# Second argument contains integer B.
#
# Output Format
# Return the index of the first element of the subarray of size B that has least average.
# Array indexing starts from 0.
# Input 1:
#
# A = [3, 7, 90, 20, 10, 50, 40]
# B = 3
# O/P: 3

def solve(A, B):
    n = len(A)
    min_avg = sum(A)
    index = 0
    pf_sum = [A[0]]
    for i in range(1, n):
        pf_sum.append(pf_sum[i - 1] + A[i])

    for i in range(0, n - B + 1):
        if i == 0:
            sum_val = pf_sum[B - 1]
        else:
            sum_val = pf_sum[i + B - 1] - pf_sum[i - 1]

        val = sum_val / B
        if val < min_avg:
            min_avg = val
            index = i

    return index


res = solve([3, 7, 90, 20, 10, 50, 40], 3)
print(res)

# Brute Force: O(n ^ 2)
# def solve(A, B):
#     n = len(A)
#     min_avg = sum(A)
#     index = 0
#
#     for i in range(0, n - B + 1):
#         sum_val = 0
#         for j in range(i, i + B):
#             # print(f"{i}, {j}")
#             sum_val += A[j]
#
#         val = sum_val // B
#         # print(val)
#         if min_avg > val:
#             min_avg = val
#             index = i
#
#     return index