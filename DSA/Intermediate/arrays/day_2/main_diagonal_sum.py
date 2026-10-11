# Problem Description
# You are given a N X N integer matrix.
# You have to find the sum of all the main diagonal elements of A.
#
# Main diagonal of a matrix A is a collection of elements A[i, j] such that i = j.
# Input Format
# There are 1 lines in the input.
# First 2 integers R, C are the number of rows and columns.
# Then R * C integers follow corresponding to the rowwise numbers in the 2D array A.
#
#
#
# Output Format
# Return an integer denoting the sum of main diagonal elements.
# 3 3 1 -2 -3 -4 5 -6 -7 -8 9

def solve(A):
    n = len(A)
    sum_val = 0
    for i in range(n):
        sum_val += A[i][i]

    return sum_val

res = solve([[1,2,3,4],[5,6,7,8],[9,2,3,4],[1,5,2,3]])
print(res)