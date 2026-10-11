# Problem Description
# You are given a 2D matrix A of integers.
#
# Your task is to compute the sum of elements in each row and return a 1D array where
# each element represents the sum of a corresponding row in the matrix.
# Input Format
# First argument A is a 2D array of integers.(2D matrix).
#
# Output Format
# Return an array containing row-wise sums of original matrix.
# [1,2,3,4]
# [5,6,7,8]
# [9,2,3,4]

def solve(A):
    n = len(A)
    m = len(A[0])
    row_sums = []

    for i in range(n):
        sum_val = 0
        for j in range(m):
            sum_val += A[i][j]
        row_sums.append(sum_val)

    return row_sums

res = solve(
[[1,2,3,4],
[5,6,7,8],
[9,2,3,4]]
)
print(res)