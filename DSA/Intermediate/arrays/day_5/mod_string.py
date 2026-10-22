# Problem Description
# You are given a large number in the form of a string A
# where each character denotes a digit of the number.
# You are also given a number B. You have to find out the value of A % B and return it.
# Input Format
# The first argument is a string A.
# The second argument is an integer B.
# Output Format
# Return a single integer denoting the value of A % B.
# A = "143"
# B = 2
# 1
# A = "43535321"
# B = 47
# 20

def solve(A, B):
    exp = 1
    ans = 0
    a = list(map(int, A))
    n = len(A)

    # For each digit in A from last, We multiply with 10 ^ i and do modulo B
    # Carry forward the exp % B instead of doing modulo every time
    # So first value * 10 ^ i modulo B
    # Then add to the ans and modulo B
    # Then update exp and modulo B
    for i in range(n - 1, -1, -1):
        temp = a[i]
        temp = (temp * exp) % B
        ans = (ans + temp) % B
        exp = (exp * 10) % B

    return ans


# res = solve("143", 2)
res = solve("43535321", 47)
print(res)