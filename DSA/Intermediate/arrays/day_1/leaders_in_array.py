# Problem Description
# Given an integer array A containing N distinct integers, you have to find all the leaders in array A. An element is a leader if it is strictly greater than all the elements to its right side.
# NOTE: The rightmost element is always a leader.
# Problem Constraints
# 1 <= N <= 105
# 1 <= A[i] <= 108
#
# Input Format
# There is a single input argument which a integer array A
#
# Output Format
# Return an integer array denoting all the leader elements of the array.

def solve(A):
    n = len(A)
    leaders = 1
    max_val = A[n - 1]
    leaders_array = [max_val]
    for i in range(n - 2, -1, -1):
        if A[i] > max_val:
            max_val = A[i]
            leaders += 1
            leaders_array.append(A[i])

    return leaders_array

res = solve([16, 17, 4, 3, 5, 2])
print(res)