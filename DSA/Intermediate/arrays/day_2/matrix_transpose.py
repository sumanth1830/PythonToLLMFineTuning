# Problem Description
# Given a 2D integer array A, return the transpose of A.
#
# The transpose of a matrix is the matrix flipped over its main diagonal,
# switching the matrix's row and column indices.
# Problem Constraints
# 1 <= A.size() <= 1000
# 1 <= A[i].size() <= 1000
# 1 <= A[i][j] <= 1000
#
# Input Format
# First argument is a 2D matrix of integers.
#
# Output Format
# You have to return the Transpose of this 2D matrix.
# A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

# Square Matrix Transpose
def solve(A):
    n = len(A)
    # Loop over the lower/upper triangle half of the matrix
    # Swap the elements

    for i in range(0, n):
        for j in range(i + 1, n):
            temp = A[i][j]
            A[i][j] = A[j][i]
            A[j][i] = temp


    return A


def rectangle_transpose(A):
    n = len(A)
    m = len(A[0])
    B = [[0] * n for _ in range(m)]
    # print(B)

    for i in range(n):
        for j in range(m):
            # When looping row wise, we add to cols
            B[j][i] = A[i][j]
            # when looping over cols
            # B[i][j] = A[j][i]

    return B

# res = solve([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
res = rectangle_transpose([[1, 2, 3, 5],[4, 5, 6, 9],[7, 8, 9, 3]])
print(res)