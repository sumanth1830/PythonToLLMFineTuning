# Write a program to input an integer T and then
# for each test case input two integers A and B in two different lines and
# then print T lines containing Least Common Multiple (LCM) of two given 2 numbers A and B.
# Note: LCM of two integers is the smallest positive integer divisible by both.
# The first line contains T which means number of test cases.
# Next 2T lines contains input A and B for each testcase.
# First line of each testcase contain an integer A and second line of the testcase contains input B.
# Output Format
# T lines each containing an integer representing LCM of A & B.
# I/P
# 3
# 2
# 3
# 9
# 6
# 2
# 6

# Op:
# 6
# 18
# 6

def main():
    t = int(input())
    for j in range(t):
        A = int(input())
        B = int(input())
        G = 1

        for i in range(1, min(A, B) + 1):
            if A % i == 0 and B % i == 0:
                G = i

        L = (A * B) // G
        print(L)

    return 0

if __name__ == '__main__':
    main()