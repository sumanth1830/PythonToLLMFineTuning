# Given an integer array A of size N, find the first repeating element in it.
# We need to find the element that occurs more than once and
# whose index of the first occurrence is the smallest.
# If there is no repeating element, return -1.

def solve(A):
    n = len(A)
    hashmap = {}
    for i in range(n):
        if hashmap.get(A[i], 0):
            hashmap[A[i]] += 1
        else:
            hashmap[A[i]] = 1

    for i in range(n):
        if hashmap[A[i]] > 1:
            return A[i]

    return -1

res = solve([10, 5, 3, 4, 3, 5, 6])
print(res)