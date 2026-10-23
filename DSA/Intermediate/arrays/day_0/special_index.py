# Problem Description
#
# Given an array, arr[] of size N, the task is to find the count of array indices such that removing an element
# from these indices makes the sum of even-indexed and odd-indexed array elements equal.
# Input Format
# First argument contains an array A of integers of size N
#
# Output Format
# Return the count of array indices such that removing an element from these indices
# makes the sum of even-indexed and odd-indexed array elements equal.
# A = [2, 1, 6, 4, 5, 9, 8]

def solve(A):
    n = len(A)
    pf_even = [A[0]]
    pf_odd = [0]
    count = 0

    for i in range(1, n):
        if i % 2 == 0:
            pf_even.append(pf_even[i - 1] + A[i])
            pf_odd.append(pf_odd[i - 1])
        else:
            pf_odd.append(pf_odd[i - 1] + A[i])
            pf_even.append(pf_even[i - 1])

    print(pf_odd)
    print(pf_even)
    for i in range(0, n):
        if i == 0:
            even_val = pf_odd[-1] - pf_odd[i]
            odd_val = pf_even[-1] - pf_even[i]
        else:
            even_val = pf_even[i - 1] + pf_odd[n - 1] - pf_odd[i]
            odd_val = pf_odd[i - 1] + pf_even[n - 1] - pf_even[i]


        if even_val == odd_val:
            count += 1

    return count


res = solve([2, 1, 6, 4, 5, 9, 8])
print(res)
# [2, 1, 6, 4, 5, 9, 8]
# [0, 1, 1, 5, 5, 14, 14]
# [2, 2, 8, 8, 13, 13, 21]
