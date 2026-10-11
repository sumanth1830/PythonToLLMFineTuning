# You are given a n x n 2D matrix A representing an image.
# Rotate the image by 90 degrees (clockwise).
# You need to do this in place.
# Note: If you end up using an additional array, you will only receive partial score.
# Input Format
# First argument is a 2D matrix A of integers
#
# Output Format
# Return the 2D rotated matrix.
# [
#     [1, 2],
#     [3, 4]
#  ]

def transpose(A):
    n = len(A)
    # Loop over the lower/upper triangle half of the matrix
    # Swap the elements

    for i in range(0, n):
        for j in range(i + 1, n):
            temp = A[i][j]
            A[i][j] = A[j][i]
            A[j][i] = temp


    return A

def solve(A):
    n = len(A)
    A_T = transpose(A)
    # print(A_T)

    for i in range(0, n):
        # Loop over each row
        # Swap elements until we reach the middle of array
        # To avoid swapping two times
        # j = n - 1
        # k = 0
        # while k < j:
        #     temp = A[i][j]
        #     A[i][j] = A[i][k]
        #     A[i][k] = temp
        #     k += 1
        #     j -= 1
        for j in range(0, int(n / 2)):
            temp = A[i][j]
            A[i][j] = A[i][n - i - 1]
            A[i][n - i - 1] = temp

    # Swapping Col wise
    # for i in range(0, int(n / 2)):
    #     for j in range(0, n):
    #         temp = A[j][i]
    #         A[j][i] = A[j][n - i - 1]
    #         A[j][n - i - 1] = temp

    return A

    return A_T

res = solve([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(res)