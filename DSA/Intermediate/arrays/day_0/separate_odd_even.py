# Problem Description
# You are given an integer T denoting the number of test cases. For each test case, you are given an integer array A.
# You have to print the odd and even elements of array A in 2 separate lines.
# NOTE: Array elements should have the same relative order as in A.
#
# Input Format
# First line of the input contains a single integer T.
#
# For each test case:
# First line consists of a single integer |A| denoting the length of array.
# Second line consists of |A| space separated integers denoting the elements of array A.
#
# Output Format
#
# For each test case:
# First line should contain an array of space separated integers containing all
# the odd elements of array A
# Second line should contain an array of space separated integers containing all
# the even elements of array A

def main():
    num_tests = int(input())
    for i in range(0, num_tests):
        arr_len = int(input())
        arr = list(map(int, input().split()))

        even_numbers = []
        odd_numbers = []
        for j in range(0, arr_len):
            if arr[j] % 2 == 0:
                even_numbers.append(arr[j])
            else:
                odd_numbers.append(arr[j])

        # print(*odd_numbers, end=" " if odd_numbers else "")
        # print()
        # print(*even_numbers, end=" " if even_numbers else "")
        # print()
        for k in odd_numbers:
            print(k, end=" ")

        print()
        for k in even_numbers:
            print(k, end=" ")
        print()


if __name__ == '__main__':
    main()