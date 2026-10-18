# Given an array A of N integers.
# Find the largest continuous sequence in a array which sums to zero.
# Input Format
# Single argument which is an integer array A.
# Output Format
# Return an array denoting the longest continuous sequence with total sum of zero.
# NOTE : If there are multiple correct answers, return the sequence which occurs first in the array.
# A = [1,2,-2,4,-4]
# O/P: [2,-2,4,-4]

def solve(A):
    n = len(A)
    pf_sum = [A[0]]
    hashmap = {}

    for i in range(1, n):
        pf_sum.append(A[i] + pf_sum[i - 1])

    max_sequence = 0
    print(pf_sum)
    for i in range(n):
        if pf_sum[i] in hashmap:
            max_sequence = max(max_sequence, i - hashmap[pf_sum[i]][0])
            # print(i - hashmap[pf_sum[i]])
            hashmap[pf_sum[i]].append(i)
        else:
            hashmap[pf_sum[i]] = [i]

    print(hashmap)

    last_zero = 0
    for i in range(n):
        if pf_sum[i] == 0:
            last_zero = i
            max_sequence = max(max_sequence, last_zero + 1)

    if 0 in hashmap and last_zero + 1 == max_sequence:
        return A[:last_zero + 1]

    print(max_sequence)
    for key in hashmap.keys():
        if hashmap[key][-1] - hashmap[key][0] == max_sequence:
            return A[hashmap[key][0]+1: hashmap[key][-1]+1]

    return max_sequence


# res = solve([3, 1, 2, -2, 4, -4, 0, 5, -5])
res = solve([15,-25,10,-8,-15,14,-11,12,25,26,-15,-23,-7,-7,20,21,-7,-15])
# res = solve([1, 2, -3, 3])
print(res)

# def solve(A):
#     n = len(A)
#     pf_sum = [A[0]]
#     hashmap = {}
#
#     for i in range(1, n):
#         pf_sum.append(A[i] + pf_sum[i - 1])
#
#     max_sequence = 0
#     print(pf_sum)
#     for i in range(n):
#         if pf_sum[i] in hashmap:
#             max_sequence = max(max_sequence, i - hashmap[pf_sum[i]])
#             # print(i - hashmap[pf_sum[i]])
#         else:
#             hashmap[pf_sum[i]] = i
#
#         # print(hashmap)
#
#     last_zero = 0
#     for i in range(n):
#         if pf_sum[i] == 0:
#             last_zero = i
#
#     if 0 in hashmap:
#         max_sequence = max(max_sequence, last_zero + 1)
#
#     return max_sequence