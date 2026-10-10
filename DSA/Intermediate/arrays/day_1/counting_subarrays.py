# Problem Description
#
# Given an array A of N non-negative numbers and a non-negative number B,
# you need to find the number of subarrays in A with a sum less than B.
# We may assume that there is no overflow.
# Problem Constraints
# 1 <= N <= 5 x 103
# 1 <= A[i] <= 1000
# 1 <= B <= 107
#
#
#
# Input Format
# First argument is an integer array A.
# Second argument is an integer B.
#
#
#
# Output Format
# Return an integer denoting the number of subarrays in A having sum less than B.
#  A = [1, 11, 2, 3, 15]
#  B = 10

def solve(A, B):
    n = len(A)
    count = 0

    for i in range(n):
        sum_val = 0
        for j in range(i, n):
            sum_val += A[j]
            if sum_val < B:
                count += 1

    return count