# Problem Description
#
# Given an array of integers A,
# every element appears twice except for one. Find that integer that occurs once.
#
# NOTE: Your algorithm should have a linear runtime complexity.
# Could you implement it without using extra memory?

def solve(A):
    n = len(A)
    val = A[0]
    # n ^ n = 0
    # so we xor out duplicates, return final val
    for i in range(1, n):
        val ^= A[i]

    return val


res = solve([1, 2, 2, 3, 1])
print(res)