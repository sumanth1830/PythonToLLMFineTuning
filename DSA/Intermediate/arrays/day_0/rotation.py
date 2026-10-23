# Given an integer array A of size N and an integer B,
# you have to print the same array after rotating it B times towards the right.
# Input Format
# There are 2 lines in the input
# Line 1: The first number is the size N of the array A.
# Then N numbers follow which indicate the elements in the array A.
# Line 2: A single integer B.
#
#
# Output Format
# Print array A after rotating it B times towards the right.

# Logic
# To the right, unlike the left
# 1 2 3 4 5 - Rotate 2 to the right
# 3 4 5 1 2
# Swap from 0 to N - k - 1 (2)
# 3 2 1 4 5
# Swap from N - k (3) to N - 1
# 3 2 1 5 4
# Swap from 0 to N - 1
# 4 5 1 2 3

def swap(arr, start, end):
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp

        start += 1
        end -= 1

    return arr


def main():
    A = list(map(int, input().split(" ")))
    B = int(input())
    N = A[0]
    A = A[1:]
    B = B % N

    # A = solve(A, 0, N - B - 1)
    # A = solve(A, N - B, N - 1)
    # A = solve(A, 0, N - 1)
    A = swap(A, 0, N - 1)
    print(A)
    A = swap(A, B, N - 1)
    print(A)
    A = swap(A, 0, B - 1)
    print(A)
    # print(f"After initial swap {A}")

    return A


if __name__ == "__main__":
    res = main()
    print(res)

