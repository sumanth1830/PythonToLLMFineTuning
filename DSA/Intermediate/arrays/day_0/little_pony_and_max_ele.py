# Problem Description
# Little Ponny is given an array, A, of N integers. In a particular operation, he can set any element of the array equal to -1.
# He wants your help in finding out the minimum number of operations required
# such that the maximum element of the resulting array is B. If it is not possible, then return -1.
# Input Format
# The first argument of input contains an integer array, A.
# The second argument of input contains an integer, B.

def solve(A, B):
    n = len(A)
    max_elements = 0
    flag = True
    for i in range(0, n):
        if A[i] > B:
            max_elements += 1

        if A[i] == B:
            flag = False

    if flag:
        return -1

    return max_elements


res = solve([2, 4, 3, 1, 5], 7)
print(res)