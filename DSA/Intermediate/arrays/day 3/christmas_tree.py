# Problem Description
# You are given an array A consisting of heights of Christmas trees and an
# array B of the same size consisting of the cost of each of the trees
# (Bi is the cost of tree Ai, where 1 ≤ i ≤ size(A)), and you are supposed to choose 3 trees
# (let's say, indices p, q, and r), such that Ap < Aq < Ar, where p < q < r.
# The cost of these trees is Bp + Bq + Br.
# You are to choose 3 trees such that their total cost is minimum. Return that cost.
# If it is not possible to choose 3 such trees return -1.
# Problem Constraints
#
# 1 <= A[i], B[i] <= 109
# 3 <= size(A) = size(B) <= 3000
# Input Format
# First argument is an integer array A.
# Second argument is an integer array B.
# Output Format
# Return an integer denoting the minimum cost of choosing 3 trees whose heights
# are strictly in increasing order, if not possible, -1.
# Input 2:
#  A = [1, 6, 4, 2, 6, 9]
#  B = [2, 5, 7, 3, 2, 7]
# Output 2:
#  7


def solve(A, B):
    n = len(A)
    # A = heights
    # B = Cost
    # 3 trees whose heights are lesser than the one to the right
    # indices should also follow same pattern
    # B is more of a cost tree

    # To optimize, we shall have a single loop over left first and then right
    # We store the min possible sum for each index i + j
    # We do the same for each index i + j + k when we are traversing right
    min_possible_sum = [0 for _ in range(n)]
    set_left_flag = False
    set_right_flag = False
    # traversing left
    # To reduce SC: O(n) to O(1)
    # Instead of maintaining an array, we can use a single variable to track
    # As we need min sum, maybe min sum left, min sum right for each i
    # Then compute min sum at the end of loop combining both
    for i in range(1, n-1):
        # print(f"i: {i}")
        min_sum_left = sum(B)
        for j in range(i-1, -1, -1):
            if A[j] < A[i]:
                # print(B[i] + B[j])
                min_sum_left = min(B[i] + B[j], min_sum_left)
                set_left_flag = True

        min_possible_sum[i] = min_sum_left
        # print(f"After Left:")
        # print(min_possible_sum)

        min_sum_right = sum(B)
        for k in range(i+1, n):
            if A[k] > A[i]:
                # print(k, A[k], A[i], B[k], min_sum_right, min_possible_sum[i] + B[k])
                min_sum_right = min(min_possible_sum[i] + B[k], min_sum_right)
                set_right_flag = True


        min_possible_sum[i] = min_sum_right
        # print(min_possible_sum)

        # print(set_right_flag)
        # print(set_left_flag)

    if not set_left_flag or not set_right_flag:
        return -1

    final_min_sum = sum(B)
    for i in range(1, n-1):
        final_min_sum = min(final_min_sum, min_possible_sum[i])

    return final_min_sum


# res = solve([1, 6, 4, 2, 6, 9], [2, 5, 7, 3, 2, 7])
res = solve([5, 3, 5], [1, 2, 3])
# res = solve([5, 9, 10, 4, 7, 8], [5, 6, 4, 7, 2, 5])
print(res)

# Brute Force
# # Find all the pairs - O(n^3)
#     # Find min(cost, min_cost) for all pairs
#     # Same approach -> Find max and min to the left and right
#     # Compute cost
#     # TLE
#     min_cost = sum(B)
#     set_flag = False
#     for i in range(1, n-1):
#         # print(f"i: {i}")
#         cost = 0
#         for j in range(i-1, -1, -1):
#             # print(f"j: {j}")
#             if A[j] < A[i]:
#                 cost += B[j] + B[i]
#                 for k in range(i+1, n):
#                     # print(f"k: {k}")
#                     if A[k] > A[i]:
#                         # print(i, j , k)
#                         cost += B[k]
#                         min_cost = min(min_cost, cost)
#                         set_flag = True
#                         cost -= B[k]
#
#                 cost -= B[j] + B[i]
#
#     if not set_flag:
#         return -1
#
#     return min_cost

# Most Efficient Approach
# Using two variable to track instead of a list
# sum_val = 1000000000
# n = len(A)
#
# for i in range(1, n-1):
#     left_small = 1000000000
#     right_small = 1000000000
#
#     for j in range(i - 1, -1, -1):
#         if A[j] < A[i]:
#             left_small = min(B[j], left_small)
#
#     for k in range(i+1, n):
#         if A[i] < A[k]:
#             right_small = min(B[k], right_small)
#
#     sum_val = min(B[i] + left_small + right_small, sum_val)
#
# if sum_val != 1000000000:
#     return sum_val
# else:
#     return -1