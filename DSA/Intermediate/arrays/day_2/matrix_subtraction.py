# You are given two integer matrices A and B having same size(Both having same number of rows (N) and columns (M).
# You have to subtract matrix B from A and return the resultant matrix. (i.e. return the matrix A - B).
#
# If A and B are two matrices of the same order (same dimensions).
# Then A - B is a matrix of the same order as A and B and its elements are obtained
# by doing an element wise subtraction of A from B.
# Input Format
# The first argument is the 2D integer array A
# The second argument is the 2D integer array B
#
# Output Format
# Return a 2D matrix denoting A - B.
# A =  [[1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]]
#
# B =  [[9, 8, 7],
#       [6, 5, 4],
#       [3, 2, 1]]

def solve(A, B):
    n = len(A)
    m = len(A[0])

    for i in range(n):
        for j in range(m):
            A[i][j] -= B[i][j]


    return A

res = solve(
[[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]],
[[9, 8, 7],
      [6, 5, 4],
      [3, 2, 1]]
)
print(res)