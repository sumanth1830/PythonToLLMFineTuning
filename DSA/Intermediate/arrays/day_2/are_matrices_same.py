# You are given two matrices A and B of equal dimensions and you have to check
# whether two matrices are equal or not.
# NOTE: Both matrices are equal if A[i][j] == B[i][j] for all i and j.
# Input Format
# First argument is 2-D array of integers representing matrix A.
# Second argument is 2-D array of integers representing matrix B.
#
# Output Format
# Return 1 if both matrices are equal or return 0.
# A = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# B = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]

def solve(A, B):
    n = len(A)
    m = len(A[0])

    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]:
                return 0

    return 1