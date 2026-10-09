# Problem Description
# You are given an array A of integers of size N.
# Your task is to find the equilibrium index of the given array
# The equilibrium index of an array is an index such that the sum of elements at lower indexes
# is equal to the sum of elements at higher indexes.
# If there are no elements that are at lower indexes or at higher indexes,
# then the corresponding sum of elements is considered as 0.
#
# Note:
#
#     Array indexing starts from 0.
#     If there is no equilibrium index then return -1.
#     If there are more than one equilibrium indexes then return the minimum index.

# Input Format
# First arugment is an array A .
#
# Output Format
# Return the equilibrium index of the given array. If no such index is found then return -1.

# A = [-7, 1, 5, 2, -4, 3, 0]
# O/P: 3


def solve(A):
    n = len(A)
    pf_sum = [A[0]]

    for i in range(1, n):
        val = pf_sum[i - 1] + A[i]
        pf_sum.append(val)

    # print(pf_sum)

    for i in range(0, n):
        if i == 0:
            left_val = 0
        else:
            left_val = pf_sum[i - 1]
        right_val = pf_sum[n - 1] - pf_sum[i]
        if left_val == right_val:
            return  i

    return -1

res = solve([-7, 1, 5, 2, -4, 3, 0])
print(res)