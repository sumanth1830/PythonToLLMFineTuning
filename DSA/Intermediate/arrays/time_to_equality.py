# Problem Description
# Given an integer array A of size N. In one second, you can increase the value of one element by 1.
# Find the minimum time in seconds to make all elements of the array equal.
# Input Format
# First argument is an integer array A.
#
# Output Format
# Return an integer denoting the minimum time to make all elements equal.
# A = [2, 4, 1, 3, 2]

def solve(A):
    # Find max element and diff of max element and rest
    # That's the answer
    n = len(A)
    max_val = 0
    sum_val = 0
    for i in range(0, n):
        if max_val < A[i]:
            max_val = A[i]

    for i in range(0, n):
        sum_val += max_val - A[i]

    return sum_val


res = solve([2, 4, 1, 3, 2])
print(res)