# Problem Description
# You are given an array of integers A of size N.
# Return the difference between the maximum among all even numbers of A and the minimum among all odd numbers in A.
# Input Format
# The first argument given is the integer array, A.
#
#
#
# Output Format
# Return maximum among all even numbers of A - minimum among all odd numbers in A.


def solve(A):
    # Diff of Max of all even and min among odd numbers
    n = len(A)
    max_even = -9999999999
    min_odd = 9999999999
    for i in range(0, n):
        if A[i] % 2 == 0 and A[i] > max_even:
            max_even = A[i]

        if A[i] % 2 == 1 and A[i] < min_odd:
            min_odd = A[i]

    # print(max_even)
    # print(min_odd)
    return max_even - min_odd

res = solve([-15,-45,43,23,-63,69,35,19,37,-52])
print(res)