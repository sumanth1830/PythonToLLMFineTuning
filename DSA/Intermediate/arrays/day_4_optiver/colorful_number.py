# Given a number A, find if it is COLORFUL number or not.
# If number A is a COLORFUL number return 1 else, return 0.
# What is a COLORFUL Number:
# A number can be broken into different consecutive sequence of digits.
# The number 3245 can be broken into sequences like 3, 2, 4, 5, 32, 24, 45, 324, 245 and 3245.
# This number is a COLORFUL number,
# since the product of every consecutive sequence of digits is different
# Input Format
# The first and only argument is an integer A.
# Output Format
# Return 1 if integer A is COLORFUL else return 0.
# A = 23
# 1

def solve(A):
    A = str(A)
    val = {}

    for i in range(0, len(A)):
        for j in range(i, len(A)):
            product = 1
            for k in range(i, j + 1):
                product *= int(A[k])

            if val.get(product, 0):
                return 0
            else:
                val[product] = 1

    return 1



res = solve(23)
print(res)