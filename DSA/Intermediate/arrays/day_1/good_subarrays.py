# Problem Description
# Given an array of integers A, a subarray of an array is said to be good if it fulfills any one of the criteria:
# 1. Length of the subarray is be even, and the sum of
# all the elements of the subarray must be less than B.
# 2. Length of the subarray is be odd, and the sum of
# all the elements of the subarray must be greater than B.
# Your task is to find the count of good subarrays in A.
# Input Format
# The first argument given is the integer array A.
# The second argument given is an integer B.
#
# Output Format
# Return the count of good subarrays in A.
# A = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9]
# B = 65
# Output
# 36

def solve(A, B):
    n = len(A)
    count = 0

    for i in range(n):
        sum_val = 0
        for j in range(i, n):
            length = j - i + 1
            sum_val += A[j]
            if (length % 2 == 0 and sum_val < B) or (length % 2 == 1 and sum_val > B):
                count += 1

    return count

res = solve([13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9], 65)
print(res)