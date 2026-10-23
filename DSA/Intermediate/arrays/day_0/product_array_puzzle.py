# Given an array of integers A, find and return the product array of the same size
# where the ith element of the product array will be equal to the product of all
# the elements divided by the ith element of the array.
#
# Note: It is always possible to form the product array with integer (32 bit) values.
# Solve it without using the division operator.

# Input Format
# The only argument given is the integer array A.
#
# Output Format
# Return the product array.
#
# Constraints
# 2 <= length of the array <= 1000
# 1 <= A[i] <= 10
# A = [1, 2, 3, 4, 5]
# O/P: [120, 60, 40, 30, 24]

def solve(A):
    n = len(A)
    product_val = 1
    for i in range(0, n):
        product_val *= A[i]

    for i in range(0, n):
        A[i] = product_val // A[i]

    return A


res = solve([1, 2, 3, 4, 5])
print(res)