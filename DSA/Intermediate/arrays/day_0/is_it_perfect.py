"""
Problem Description
Given the Number of Test Cases as T,
For each test case, take an integer N as input, you have to tell whether it is a perfect number or not.
A perfect number is a positive integer that is equal to the sum of its proper positive divisors (excluding the number itself).
A positive proper divisor divides a number without leaving any remainder.


Problem Constraints
1 <= T <= 10
1 <= N <= 10 ^ 6


Input Format
The first line of the input contains a single integer T.
Each of the next T lines contains a single integer N.

Output Format
For each testcase, print YES if the given integer is perfect, else print NO, in a separate line


Example Input
Input 1:
2
4
6

Input 2:
1
3


Example Output
Output 1:
NO
YES

Output 2:
NO
"""

def main():
    num_test_cases = int(input())
    for i in range(0, num_test_cases):
        A = int(input())
        val = A // 2 + 1
        total = 0
        for j in range(1, val):
            if A % j == 0:
                total += j

        if total == A:
            print("YES")
        else:
            print("NO")

    return None


if __name__ == "__main__":
    res = main()
    print(res)