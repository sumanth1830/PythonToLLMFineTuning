# Problem Description
# Given an array of integers A of size N and an integer B, determine whether the element B exists in the array A or not.
# If it exists, print 1; otherwise, print 0. This needs to be processed for T independent test cases.
# Input Format
# The first line contains an integer T, representing the number of test cases.
# For each test case:
#
#     The first line contains an integer N, representing the size of the array.
#     The second line contains N space-separated integers representing the elements of array A.
#     The third line contains an integer B, representing the element to be searched.
#
# Output Format
# For each test case, print on a separate line 1 if the element exists, else print 0.

def main():
    num_test_cases = int(input())

    for test_case in range(num_test_cases):
        arr_len = int(input())
        arr = list(map(int, input().split()))
        search_element = int(input())
        flag = True
        for ele in arr:
            if search_element == ele:
                print(1)
                flag = False
                break

        if flag:
            print(0)


if __name__ == "__main__":
    main()
