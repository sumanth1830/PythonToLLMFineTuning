# Problem Description
# Given an integer A. Unset B bits from the right of A in binary.
#
# For example, if A = 93 and B = 4, the binary representation of A is 1011101.
# If we unset the rightmost 4 bits, we get the binary number 1010000,
# which is equal to the decimal value 80.
# Input Format
# The first argument is a single integer A.
# The second argument is a single integer B.
# Output Format
# Return the number with B unset bits from the right.
# A = 25, B = 3
# O/P: 24

def solve(A, B):
    # unset B bit from the right of A
    # 0 0 0 1 1 0 0 1 - 25
    # 0 0 0 1 1 0 0 0 - 24
    ans = A
    for i in range(B):
        # We are finding if the bit is set or not and then
        # unsetting it by subtracting
        if A & (1 << i):
            ans -= (1 << i)
    return ans



res = solve(25, 3)
print(res)