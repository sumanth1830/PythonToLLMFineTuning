# Problem Description
# You are given a constant array A.
# You are required to return another array which is the reversed form of the input array.

def reverse(A):
    i = 0
    j = len(A) - 1

    while i < j:
        temp = A[j]
        A[j] = A[i]
        A[i] = temp

        i += 1
        j -= 1

    return A

res = reverse([1,2,3,2,7])
print(res)