# Problem Description
# Given an array of integers A, of size N.
# Return the maximum size subarray of A having only non-negative elements.
# If there are more than one such subarray, return the one having the smallest starting index in A.
# NOTE: It is guaranteed that an answer always exists.
# Input Format
# The first and only argument given is the integer array A.
# Output Format
# Return maximum size subarray of A having only non-negative elements.
# If there are more than one such subarrays, return the one having earliest starting index in A.
# Input
# A = [5, 6, -1, 7, 8]
# Output
# [5, 6]

def solve(A):
    n = len(A)
    max_size = 0
    max_size_index = 0
    # Observation: subarray lies on the left of the negative number
    ret = [[]]
    for i in A:
        if i < 0:
            ret.append([])
        else:
            ret[-1].append(i)

    max_len = max([len(i) for i in ret])

    for i in ret:
        if len(i) == max_len:
            return i

    return None


# res = solve([5, 6, -1, 7, 8])
# res = solve([1, 2, 3, 4, 5, 6])
# res = solve([8986143,-5026827,5591744,4058312,2210051,5680315,-5251946,-607433,1633303,2186575])
res = solve([-4549634,-3196682,8455838,-1432628,-263819,-3928366,-5556259,-2114783,3923939,-4183708])
print(res)

# Brute Force in a way
# n = len(A)
#     max_size = 0
#     max_size_index = 0
#     # Observation: subarray lies on the left of the negative number
#     for i in range(n):
#         if A[i] > 0:
#             if max_size == 0:
#                 max_size = 1
#                 max_size_index = i
#
#             for j in range(i+1, n):
#                 if A[j] > 0:
#                     if max_size <  j - i + 1:
#                         max_size = j - i + 1
#                         max_size_index = i
#                 else:
#                     break
#
#             print(i, max_size, max_size_index)
#
#
#     print(max_size_index)
#     print(max_size)
#
#     return A[max_size_index:max_size_index+max_size]