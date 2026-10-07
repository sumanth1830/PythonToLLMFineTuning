# Problem Description
#
# Given an array A and an integer B. A pair(i, j) in the array is a good pair if i != j and (A[i] + A[j] == B).
# Check if any good pair exist or not.
# Problem Constraints
# 1 <= A.size() <= 10^ 4
# 1 <= A[i] <= 10 ^ 9
# 1 <= B <= 10 ^ 9
# Input Format
# First argument is an integer array A.
# Second argument is an integer B.
#
# Output Format
# Return 1 if good pair exist otherwise return 0.

"""
1) Brute Force
Two For Loops, checking every combination N^2

2) Only Upper Trianle/Lower Triangle
i: 0 to N, j: 0 to i
i: 0 to N, j: i to N

Still N^2 approach

3) Using a Dictionary to store A elements as keys
O(N) as
"""

# def solve(A, B):
#     N = len(A)
#     for i in range(0, N):
#         for j in range(0, i):
#             if A[i] + A[j] == B and i != j:
#                 return 1
#
#     return 0

def solve(A, B):
    n = len(A)
    C = {}
    for i in range(0, n):
        if C.get(B - A[i]):
            return 1
        else:
            C[A[i]] = A[i]

    return 0

if __name__ == "__main__":
    s = solve([1,2,3,4], 7)
    print(s)