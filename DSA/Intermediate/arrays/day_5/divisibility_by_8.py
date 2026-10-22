# Problem Description
# You are given a number A in the form of a string.
# Check if the number is divisible by eight or not.
# Return 1 if it is divisible by eight else, return 0.
# Input Format
# The only argument given is a string A.
# Output Format
# Return 1 if it is divisible by eight else return 0.
# A = "16"
# 1

def solve(A):
    n = len(A)
    s = ""
    if n <= 3:
        s = A
    else:
        s = A[n - 3] + A[n - 2] + A[n - 1]
    num = int(s)
    if num % 8 == 0:
        return 1
    return 0

res = solve("224")
print(res)