# Given an array of integers A,
# find and return whether the given array contains a non-empty subarray with a sum equal to 0.
# If the given array contains a sub-array with sum zero return 1, else return 0.
# A = [1, 2, 3, 4, 5]
# 0

def solve(A):
    n = len(A)
    pf_sum = [A[0]]
    hashmap = {}

    for i in range(1, n):
        pf_sum.append(A[i] + pf_sum[i - 1])

    for i in range(n):
        if hashmap.get(pf_sum[i], 0):
            hashmap[pf_sum[i]] += 1
        else:
            hashmap[pf_sum[i]] = 1

    for key, value in hashmap.items():
        if hashmap[key] > 1 or key == 0:
            return 1

    return 0


res = solve([1, 2, 3, 4, 5])
print(res)

# Another Approach
#    def solve(self, A):
#         d = {}
#         curr_sum = 0
#         for x in A:
#             curr_sum += x
#             if curr_sum == 0 or x == 0 or curr_sum in d:
#                 return 1
#             else:
#                 d[curr_sum] = 1
#         return 0