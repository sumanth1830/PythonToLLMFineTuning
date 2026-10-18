# Given two integer arrays, A and B of size N and M, respectively.
# Your task is to find all the common elements in both the array.
#
# NOTE:
#
#     Each element in the result should appear as many times as it appears in both arrays.
#     The result can be in any order.
#
#  A = [1, 2, 2, 1]
#  B = [2, 3, 1, 2]

def solve(A, B):
    n = len(A)
    m = len(B)
    hashmap = {}

    for i in range(n):
        if hashmap.get(A[i], 0):
            hashmap[A[i]] += 1
        else:
            hashmap[A[i]] = 1

    result = []
    for i in range(m):
        if hashmap.get(B[i], 0) != 0 and hashmap[B[i]] != 0:
            result.append(B[i])
            hashmap[B[i]] -= 1

    return result


res = solve([1, 2, 2, 1], [2, 3, 1, 2])
print(res)