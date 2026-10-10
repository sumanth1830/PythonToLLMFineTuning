# You are given an integer array A of length N comprising 0's & 1's, and an integer B.
#
# You have to tell all the indices of array A that can act as
# a center of 2 * B + 1 length 0-1 alternating subarray.
#
# A 0-1 alternating array is an array containing only 0's & 1's, and
# having no adjacent 0's or 1's. For e.g. arrays [0, 1, 0, 1], [1, 0] and [1] are 0-1 alternating,
# while [1, 1] and [0, 1, 0, 0, 1] are not.
# Input Format
# First argument is an integer array A.
# Second argument is an integer B.
#
# Output Format
# Return an integer array containing indices(0-based) in sorted order.
# If no such index exists, return an empty integer array.
# A = [0, 0, 0, 1, 1, 0, 1]
# B = 0
# [0, 1, 2, 3, 4, 5, 6]

def solve(A, B):
    n = len(A)
    arr_len = 2 * B + 1
    if arr_len == 1:
        return list(range(n))

    indexes = []
    for i in range(B, n - B):
        count = 1
        for j in range(i - B + 1, i + B + 1):
            if A[j] != A[j - 1]:
                count += 1

        if count == arr_len:
            indexes.append(i)

    return indexes

res = solve([0, 0, 0, 1, 1, 0, 1, 0, 1], 2)
# res = solve([0,1,0,1,1,1,0,1,1,1,1,0], 2)
print(res)


# Initial Approach - O(n ^ 2)
# def solve(A, B):
#     n = len(A)
#     arr_len = 2 * B + 1
#     if arr_len == 1:
#         return list(range(n))
#
#     indexes = []
#     for i in range(B, n - B):
#         j = i - 1
#         k = i + 1
#         left_count = 0
#         right_count = 0
#         # print(f"i: {i}, j: {j}, {i - B}, {i + B}")
#         while j >= i - B:
#             if A[j + 1] - A[j] != 0:
#                 left_count += 1
#             # print(f"j: {j}, left count: {left_count}")
#             j -= 1
#
#         while k <= i + B:
#             if A[k - 1] - A[k] != 0:
#                 right_count += 1
#
#             k += 1
#
#         if left_count + right_count + 1 == arr_len:
#             indexes.append(i)
#
#     return indexes