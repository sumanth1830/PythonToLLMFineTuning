# Problem Description
# Given a number A. Return square root of the number if it is perfect square otherwise return -1.
# Note: A number is a perfect square if its square root is an integer.
#
# Problem Constraints
# 1 <= A <= 10^8
#
# Input Format
# First and the only argument is an integer A.
#
# Output Format
# Return an integer which is the square root of A if A is perfect square otherwise return -1.

def main():
    A = int(input())
    val = int(A ** 0.5) + 1
    for i in range(1, val):
        if i * i == A:
            return val
    return -1

if __name__ == "__main__":
    res = main()
    print(res)