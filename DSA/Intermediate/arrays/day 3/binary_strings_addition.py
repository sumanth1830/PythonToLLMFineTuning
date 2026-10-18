# Problem Description
# Given two binary strings A and B. Return their sum (also a binary string).
# Input Format
# The two argument A and B are binary strings.
#
# Output Format
# Return a binary string denoting the sum of A and B

def solve(A, B):
    i = len(A) - 1
    j = len(B) - 1
    carry = 0
    ans = ''

    while i >= 0 or j >= 0:
        sum_val = 0
        if i >= 0:
            sum_val += int(A[i])
            i -= 1

        if j >= 0:
            sum_val += int(B[j])
            j -= 1

        # print(A[i], A[j], sum_val, int(A[i]) + int(A[j]))
        # print(sum_val)
        sum_val += carry
        bit = sum_val % 2
        carry = sum_val // 2
        ans += str(bit)
        # print(ans[::-1])
        # print(bit)

    if carry == 1:
        ans += str(carry)

    return ans[::-1]



res = solve("1", "1")
print(res)