# Problem Description
# Given an array of integers A and multiple values in B,
# which represents the number of times array A needs to be left rotated.
# Find the rotated array for each value and return the result in the from of a matrix
# where ith row represents the rotated array for the ith value in B.
# Input Format
# The first argument given is the integer array A.
# The second argument given is the integer array B.
#
#
# Output Format
# Return the resultant matrix.

def reverse(A, start, end):
    i = start
    j = end

    while i < j:
        temp = A[j]
        A[j] = A[i]
        A[i] = temp

        i += 1
        j -= 1

    return A


def solve(A, B):
    c = []
    n = len(A)
    n_b = len(B)
    # 1 2 3 4 5 6
    # 2 left rotations
    # Reverse 0 -> 2 - 1
    # 2 1 3 4 5 6
    # Reverse 2 -> n - 1
    # 2 1 6 5 4 3
    # Reverse all
    # 3 4 5 6 1 2
    # 3 4 5 6 1 2
    temp = list(A)
    for rot in B:
        k = rot % n
        A = list(temp)
        A = reverse(A, 0, k - 1)
        A = reverse(A, k, n - 1)
        A = reverse(A, 0, n - 1)

        c.append(A)
        # print(c)

    return c

res = solve([1, 2, 3, 4, 5], [2, 3])
print(res)