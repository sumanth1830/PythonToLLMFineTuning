# Problem Description
# You are given an integer array A of length N.
# You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
# For each query, you have to find the sum of all elements from L to R indices in A (0 - indexed).
# More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.
# Input Format
# The first argument is the integer array A.
# The second argument is the 2D integer array B.
#
# Output Format
# Return an integer array of length M where ith element is the answer for ith query in B.
# A = [1, 2, 3, 4, 5]
# B = [[0, 3], [1, 2]]

def solve(A, B):
    n = len(A)
    pf_sum = [A[0]]

    for i in range(1, n):
        pf_sum.append(A[i] + pf_sum[i - 1])

    m = len(B)
    range_sums = []
    for i in range(m):
        l = B[i][0]
        r = B[i][1]
        if l == 0:
            val = pf_sum[r]
        else:
            val = pf_sum[r] - pf_sum[l - 1]

        range_sums.append(val)

    return range_sums


res = solve([1, 2, 3, 4, 5], [[0, 3], [1, 2]])
print(res)