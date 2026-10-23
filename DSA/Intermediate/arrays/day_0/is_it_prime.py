# Take an integer A as input, you have to tell whether it is a prime number or not.
#
# A prime number is a natural number greater than 1 which is divisible only by 1 and itself.
# Problem Constraints
#
# 1 <= A <= 106
#
# Input Format
# First and only line of the input contains a single integer A.
#
# Output Format
# Print YES if A is a prime, else print NO.
from cmath import sqrt


# Example Input
# Input 1:
#  3
#
# Input 2:
#  4
#
# Example Output
# Output 1:
#  YES
#
# Output 2:
#  NO

def main():
    A = int(input())
    val = int(A ** 0.5)
    for i in range(2, val):
        if A % i == 0:
            return "NO"

    return "YES"


if __name__ == '__main__':
    res = main()
    print(res)