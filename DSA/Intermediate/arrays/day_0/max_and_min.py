# Take input an array A of size N and write a program to print maximum and minimum elements of the input.
# The only line of the input would contain a single integer N that represents the length of the array
# followed by the N elements of the input array A.
# 1 <= N <= 1000
# 1 <= A <= 1000

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    A = list(map(int, input().split()))
    N = A[0]
    A = A[1:]

    max_val = -1
    min_val = 1001

    for i in range(0, N):
        if A[i] > max_val:
            max_val = A[i]

        if A[i] < min_val:
            min_val = A[i]

    return max_val, min_val


if __name__ == '__main__':
    res = main()
    print(res)
