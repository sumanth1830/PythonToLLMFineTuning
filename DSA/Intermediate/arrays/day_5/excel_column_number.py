"""
Problem Description
Given a column title as appears in an Excel sheet, return its corresponding column number.

Problem Constraints
1 <= length of the column title <= 5

Input Format
The only argument is a string that represents the column title in the excel sheet.

Output Format
Return a single integer that represents the corresponding column number.
# AB
# 28
"""

def solve(A):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    A = A.lower()
    res = 0
    n = len(A)

    for i in range(n):
        # Each Alphabet * 26 indicates the starting point of the series with that alphabet
        res += pow(26, n - i - 1) * (alpha.index(A[i]) + 1)

    return res

result = solve("AB")
print(result)