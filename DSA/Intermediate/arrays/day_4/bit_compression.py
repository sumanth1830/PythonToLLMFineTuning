# Richard Hendricks, a mastermind in compression algorithms,
# is an employee of Hooli in Silicon Valley.
# One day, he finally decided to quit and work on his new idea of the middle-out compression algorithm.
#
# He needed to work at the bit - level to compress data. He, eventually, encountered this problem.
# There is an array A of N integers. He has to perform certain operations on the elements.
# In any one operation, two indices i and j (i < j) are chosen, and A[i] is replaced with A[i] & A[j],
# and A[j] is replaced with A[i] | A[j], where &
# represents the Bitwise AND operation and | represents the Bitwise OR operation.
# This operation is performed over all the pairs of integers in the array.
#
# Help Richard find the Bitwise XOR of all the elements after performing the operations.
# Input Format
# The first argument is the integer array A.
# Output Format
# Return a single integer denoting the XOR of the elements after performing the operations.
# A = [1, 3, 5]
# 7

def solve(A):
    ans = 0
    # Obs
    # The XOR of all the numbers is preserved even after performing all the operations.
    # A[i] ^ A[j] = (A[i] & A[j]) ^ (A[i] | A[j])
    for i in A:
        ans ^= i
    return ans



res = solve([1, 3, 5])
print(res)