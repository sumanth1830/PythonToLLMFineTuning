# Problem Description
#
# You are given two matrices A & B of same size,
# you have to return another matrix which is the sum of A and B.
# Input Format
# The first argument is the 2D integer array A. The second argument is the 2D integer array B
#
# Output Format
# You have to return a vector of integers after doing required operations.
# A = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# B = [[9, 8, 7],
#      [6, 5, 4],
#      [3, 2, 1]]
# O/P
# [[10, 10, 10],
#  [10, 10, 10],
#  [10, 10, 10]]

def solve(A, B):
    n = len(A)
    # Creates n completely separate list objects in memory
    C = [[0] * n for _ in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] + B[i][j]

    print(C)


res = solve(
    [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]],
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
)
