# Problem Description
# You have given a string A having Uppercase English letters.
# You have to find how many times subsequence "AG" is there in the given string.
# NOTE: Return the answer modulo 109 + 7 as the answer can be very large.
# Input Format
# First and only argument is a string A.
#
# Output Format
# Return an integer denoting the answer.
# A = "ABCGAG"

# Brute Force
# Two loops i: 0 -> n, j: i + 1 -> n
# O(n^2) approach

# Carry Forward Approach
# Use counts of A, G
# Loop over the Array
# Count the pairs

def solve(A):
    n = len(A)
    a_count = 0
    pair_count = 0
    A = A.lower()
    for i in range(n):
        if A[i] == "a":
            a_count += 1

        elif A[i] == "g":
            pair_count += a_count

    return pair_count

res = solve("ABCGAG")
print(res)