# Given an integer array A of size N. You can remove any element from the array in one operation.
# The cost of this operation is the sum of all elements in the array present before this operation.
# Find the minimum cost to remove all elements from the array.
# Input Format
# First and only argument is an integer array A.
# Output Format
# Return an integer denoting the total cost of removing all elements from the array.
# A = [2, 1]
# O/P: 4

def solve(A):
    n = len(A)
    cost = sum(A)
    A.sort(reverse=True)
    count = 0

    for i in range(0, len(A)):
        count += cost
        cost -= A[i]

    return count

res = solve([1, 6, 4])
print(res)