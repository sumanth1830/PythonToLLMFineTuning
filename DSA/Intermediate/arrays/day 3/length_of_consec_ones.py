# Problem Description
# Given a binary string A. You may perform at most one swap,
# which exchanges any one 0 of the string with any one 1 of the string.
# The two characters do not have to be next to each other.
#
# Return the length of the longest run of consecutive 1's that can be achieved.
# Input Format
# The only argument is the binary string A.
# Output Format
# Return an integer, the length of the longest run of consecutive 1's that can be achieved.
# A = "111011101"
# Output:
# 7

def solve(A):
    n = len(A)
    A = list(map(int, A))
    max_len = 0
    total_ones = 0

    for i in range(n):
        if A[i] == 1:
            total_ones += 1

    if total_ones == len(A):
        return total_ones

    for i in range(n):
        l = 0
        r = 0
        if A[i] == 0:
            for j in range(i - 1, -1, -1):
                if A[j] == 1:
                    l += 1
                else:
                    break

            for k in range(i + 1, n):
                if A[k] == 1:
                    r += 1
                else:
                    break

            if l + r == total_ones:
                return l + r

        max_len = max(max_len, l + r + 1)

    return max_len



res = solve("111011101")
res = solve("111000")
print(res)