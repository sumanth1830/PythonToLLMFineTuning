# You are given a N X N integer matrix.
# You have to find the sum of all the minor diagonal elements of A.
# Minor diagonal of a M X M matrix A is a collection of elements A[i, j]
# such that i + j = M + 1 (where i, j are 1-based).
# Input Format
# First and only argument is a 2D integer matrix A.
#
# Output Format
# Return an integer denoting the sum of minor diagonal elements.
#  A = [[1, -2, -3],
#       [-4, 5, -6],
#       [-7, -8, 9]]

def solve(A):
    n = len(A)
    sum_val = 0
    i = 0
    j = n - 1

    while j >= 0:
        sum_val += A[i][j]
        i += 1
        j -= 1

    return sum_val

res = solve(
[[1, -2, -3],
      [-4, 5, -6],
      [-7, -8, 9]]
)
print(res)