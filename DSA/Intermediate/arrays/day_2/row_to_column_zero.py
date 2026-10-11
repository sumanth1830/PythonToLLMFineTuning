# Problem Description
#
# You are given a 2D integer matrix A, make all the elements in a row or column zero
# if the A[i][j] = 0. Specifically, make entire ith row and jth column zero.
# Input Format
# First argument is a 2D integer matrix A.
# Output Format
# Return a 2D matrix after doing required operations.
# [1,2,3,4]
# [5,6,7,0]
# [9,2,0,4]

# Output
# [1,2,0,0]
# [0,0,0,0]
# [0,0,0,0]

def solve(A):
    x = 1
    y = 1
    m = len(A)
    n = len(A[0])

    # We are traversing the first row and first column to find
    # if there are any zeroes, so that we can zero out the first row and
    # column later
    for i in range(0, n):
        if A[0][i] == 0:
            x = 0

    for j in range(0, m):
        if A[j][0] == 0:
            y = 0

    # Traversing through the array
    # If any element is zero
    # The corresponding first row and first column elements are updated
    # as zeros (We are using them as trackers)
    for i in range(1, m):
        for j in range(1, n):
            if A[i][j] == 0:
                A[i][0] = 0
                A[0][j] = 0

    # Traversing the first column and zeroing the corresponding column values
    for j in range(1, n):
        if A[0][j] == 0:
            for i in range(0, m):
                A[i][j] = 0

    for i in range(1, m):
        if A[i][0] == 0:
            for j in range(0, n):
                A[i][j] = 0

    if y == 0:
        for i in range(0, m):
            A[i][0] = 0

    if x == 0:
        for j in range(0, n):
            A[0][j] = 0

    return A


# res = solve(
#     [
#         [1,2,3,4],
#         [5,6,7,0],
#         [9,2,0,4],
#     ]
# )
res = solve(
[[97,18,55,1,50,17,16,0,22,14],[58,14,75,54,11,23,54,95,33,23],[73,11,2,80,6,43,67,82,73,4],[61,22,23,68,23,73,85,91,25,7],[6,83,22,81,89,85,56,43,32,89],[0,6,1,69,86,7,64,5,90,37],[10,3,11,33,71,86,6,56,78,31],[16,36,66,90,17,55,27,26,99,59],[67,18,65,68,87,3,28,52,9,70],[41,19,73,5,52,96,91,10,52,21]]
)
print(res)

# Brute Force Approach - O (n^2)
# def solve(A):
#     n = len(A)
#     m = len(A[0])
#
#     i_indexes = []
#     j_indexes = []
#     for i in range(n):
#         for j in range(m):
#             if A[i][j] == 0:
#                 i_indexes.append(i)
#                 j_indexes.append(j)
#
#     for i in range(n):
#         for j in range(m):
#             if i in i_indexes:
#                 A[i][j] = 0
#
#             if j in j_indexes:
#                 A[i][j] = 0
#
#
#     return A

# A bit better still not good though
#     i_len = len(i_indexes)
#     j_len = len(j_indexes)
#     for i in range(i_len):
#         for j in range(n):
#             A[i_indexes[i]][j] = 0
#
#
#     for i in range(n):
#         for j in range(j_len):
#             A[i][j_indexes[j]] = 0