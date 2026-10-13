# Problem Description
# Write a program to input an integer N from user and
# print hollow diamond star pattern series of N lines.
# See example for clarifications over the pattern.
# Problem Constraints
# 1 <= N <= 1000
#
# Input Format
# First line is an integer N
#
# Output Format
# N lines containing only char '*' as per the question.
# Input 1:
# 4
#
# Output 1:
# ********
# ***  ***
# **    **
# *      *
# *      *
# **    **
# ***  ***
# ********

def solve(num):
    pattern = ""
    # Observation
    # First and last lines are complete 2 * n
    # Middle lines have the pattern of 2 stars to 2n - 2 stars being replaced with ""
    # If n = 4, 8 stars on first line
    # 2 stars in the middle at 3, 4 are replaced
    # 4 stars in the middle from 2, 5 are replaced
    # 6 stars in the middle from 1, 6 are replaced
    # 2 * n on first line
    # n - i filled with * (4 - 1) + (2i filled with '') + (n - i) filled with *
    # Then they reappear as i go pasts n
    # So we print from i : 0 to n
    # Then we redo the opposite from n - 1 to 0
    for i in range(num):
        if i == 0:
            pattern += "*" * (2 * num) + "\n"

        if i > 0:
            pattern += "*" * (num - i) + " " * 2 * i + "*" * (num - i) + "\n"

    for i in range(num - 1, -1, -1):
        if i > 0:
            pattern += "*" * (num - i) + " " * 2 * i + "*" * (num - i) + "\n"
        if i == 0:
            pattern += "*" * (2 * num) + "\n"

    print(pattern)

    return 0

res = solve(6)
