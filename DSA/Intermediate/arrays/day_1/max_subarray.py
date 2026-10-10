# Problem Description
# You are given an integer array C of size A.
# Now you need to find a subarray (contiguous elements) so that the
# sum of contiguous elements is maximum.
# But the sum must not exceed B.
# Input Format
# The first argument is the integer A.
# The second argument is the integer B.
# The third argument is the integer array C.
#
# Output Format
# Return a single integer which denotes the maximum sum.
# A = 5
# B = 12
# C = [2, 1, 3, 4, 5]
# O/P: 12

def solve(A, B, C):
    n = A
    max_sum = 0
    pf_sum = [C[0]]

    for i in range(n):
        pf_sum.append(C[i] + pf_sum[i - 1])

    for i in range(0, n):
        sum_val = 0
        for j in range(i, n):
            sum_val += C[j]
            if sum_val < B:
                max_sum = max(max_sum, sum_val)
            elif sum_val == B:
                return B

    return max_sum


res = solve(5, 12,[2, 1, 3, -4, 5])
print(res)

# Another Approach - Prefix Sum
# def maxSubarray(A, B, C):
#     max_val = 0
#     prefix_sum = [C[0]]
#
#     for i in range(1, A):
#         prefix_sum.append(C[i] + prefix_sum[i - 1])
#
#     # print(prefix_sum)
#
#     for i in range(0, A):
#         for j in range(i, A):
#             if i == 0:
#                 sum_val = prefix_sum[j]
#             else:
#                 sum_val = prefix_sum[j] - prefix_sum[i - 1]
#
#             if sum_val == B:
#                 return B
#
#             if sum_val <= B:
#                 max_val = max(max_val, sum_val)
#             # print(f"A[i:j]: {C[i:j+1]}, max_sum: {max_val}, sum_val: {sum_val}")
#
#     if max_val <= B:
#         return max_val
#
#     return 0