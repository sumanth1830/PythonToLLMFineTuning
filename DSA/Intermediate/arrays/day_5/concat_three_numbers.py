# Problem Description
# Given three 2-digit integers, A, B, and C,
# find out the minimum number obtained by concatenating them in any order.
# Return the minimum result obtained.
# Input Format
# The first argument of input contains an integer, A.
# The second argument of input contains an integer, B.
# The third argument of input contains an integer, C.
# Output Format
# Return an integer representing the answer.
#  A = 10
#  B = 20
#  C = 30
# 102030

def solve(A, B, C):
    return int(''.join([str(x) for x in sorted([A, B, C])]))


res = solve("10", "20", "30")
print(res)