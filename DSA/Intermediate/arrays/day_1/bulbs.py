# Problem Description
# A wire connects N light bulbs.
# Each bulb has a switch associated with it; however, due to faulty wiring,
# a switch also changes the state of all the bulbs to the right of the current bulb.
# Given an initial state of all bulbs,
# find the minimum number of switches you have to press to turn on all the bulbs.
# You can press the same switch multiple times.
# Note: 0 represents the bulb is off and 1 represents the bulb is on.
#
# Problem Constraints
# 0 <= N <= 5×105
# 0 <= A[i] <= 1
#
# Input Format
# The first and the only argument contains an integer array A, of size N.
#
# Output Format
# Return an integer representing the minimum number of switches required.

def solve(A):
    n = len(A)
    switch_count = 0

    for i in range(n):
        if (A[i] == 0 and switch_count % 2 == 0) or (A[i] == 1 and switch_count % 2 == 1):
            switch_count += 1

    return switch_count


# res = solve([0, 1, 1, 0, 0, 0, 1, 0, 1, 0])
res = solve([0, 1, 0, 1])
print(res)

# Similar Approach
# n = len(A)
# count = 0
# state = 0
#
# for i in range(n):
#     state = A[i]
#     if count % 2 == 0:
#         state = A[i]
#     else:
#         state = 1 - A[i]
#
#     if state == 0:
#         count += 1
#
# return count