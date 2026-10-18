# Shaggy has an array A consisting of N elements.
# We call a pair of distinct indices in that array a special if elements
# at those indices in the array are equal.
# Shaggy wants you to find a special pair such that the distance between
# that pair is minimum. Distance between two indices is defined as |i-j|.
# If there is no special pair in the array, then return -1.
# Input Format
# The first and only argument is an integer array A.
# Output Format
# Return one integer corresponding to the minimum possible distance between a special pair.
# A = [7, 1, 3, 4, 1, 7]
# O/P: 3

def solve(A):
    n = len(A)
    C = {}
    min_distance = n

    for i in range(n):
        print(C.get(A[i], 0))
        if A[i] in C:
            print(f"{min_distance}, {C[A[i]]}, {i}")
            min_distance = min(min_distance, i - C[A[i]])
            C[A[i]] = i
        else:
            C[A[i]] = i

        print(C)

    if min_distance == n:
        return -1

    return min_distance


# res = solve([7, 1, 2, 4, 1, 7])
res = solve([1, 1])
print(res)