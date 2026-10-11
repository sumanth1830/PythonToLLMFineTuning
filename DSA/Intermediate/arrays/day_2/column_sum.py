# Problem Description
#
# You are given a 2D integer matrix A,
# return a 1D integer array containing column-wise sums of original matrix.
# Input Format
# First argument is a 2D array of integers.(2D matrix).
#
# Output Format
# Return an array containing column-wise sums of original matrix.
# [1,2,3,4]
# [5,6,7,8]
# [9,2,3,4]

def solve(A):
    n = len(A)
    m = len(A[0])
    col_sums = []

    for col in range(0, m):
        sum_val = 0
        for row in range(0, n):
            sum_val += A[row][col]

        col_sums.append(sum_val)

    return col_sums

res = solve([[1,2,3,4],[5,6,7,8],[9,2,3,4]])
print(res)
