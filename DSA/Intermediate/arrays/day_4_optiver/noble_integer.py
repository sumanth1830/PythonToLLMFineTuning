# Problem Description
#
# Given an integer array A,
# find if an integer p exists in the array such that the
# number of integers greater than p in the array equals p.
# Input Format
# First and only argument is an integer array A.
# Output Format
# Return 1 if any such integer p is present else, return -1.
# A = [3, 2, 1, 3]

def solve(A):
    n = len(A)
    A.sort(reverse=True)
    # 3, 2, 1, 3
    # 3 3 2 1
    # 0 0 2 3
    more = 0
    count = 0
    if A[0] == 0:
        count += 1

    for i in range(1, n):
        if A[i] != A[i - 1]:
            more = i
        if A[i] == more:
            # print(f"i: {i}, A[i]:{A[i]}")
            return 1

    if count > 0:
        return 1
    return -1



res = solve([3, 2, 1, 3])
print(res)