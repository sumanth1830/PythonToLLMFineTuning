# Given an array B of length A with elements 1 or 0.
# Find the number of subarrays such that the bitwise OR of all the elements
# present in the subarray is 1.
# Note : The answer can be large. So, return type must be long.
# Input Format
# The first argument is a single integer A.
# The second argument is an integer array B.
# Output Format
# Return the number of subarrays with bitwise array 1.
# A = 3
# B = [1, 0, 1]
# O/P: 5

def solve(A, B):
    count = 0
    zeroes = 0

    # Obs
    # 1 of len 1 will be part of the result
    # Number of 1's for sure
    # 1 with any number of zeroes satisfy as well

    # Brute Force
    # All subarrays + Bitwise OR of all elements
    # i: 0 -> n
    # j: i -> n
    # k: i -> j
    # O(N^3)
    # calculate bitwise OR and increment count if satisfied

    # If there is 1 encountered, no need to calculate further as
    # One 1 could satisfy the criteria

    for i in range(A):
        if B[i] == 0:
            zeroes += 1
        else:
            count += zeroes * (zeroes + 1) // 2
            zeroes = 0


    count += zeroes * (zeroes + 1) // 2
    total = (A * (A + 1)) // 2

    return total - count


res = solve(3, [1, 0, 1])
print(res)