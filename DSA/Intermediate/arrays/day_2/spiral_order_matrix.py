# Problem Description
#
# Given an integer A, generate a square matrix filled with elements
# from 1 to A2 in spiral order and return the generated square matrix.
# Input Format
# First and only argument is integer A
#
# Output Format
# Return a 2-D matrix which consists of the elements added in spiral order.

# Approach
# Build all 4 outer lanes first
# Then look at the pattern on how to adapt the outer lanes to inner lane
# In this case we use a value i which starts with zero
# When the whole loop runs, we increment i, and it pushes the lanes inside in the next run
def solve(n):
    if n == 1:
        return [[1]]

    elements = [i for i in range(1, n * n + 1)]
    A = [[0] * n for _ in range(n)]

    # print(elements)
    i = 0
    index = 0
    while index < len(elements):

        row = i
        for col in range(i, n - i):
            A[row][col] = elements[index]
            index += 1

        col = n - i - 1
        for row in range(i + 1, n - i):
            A[row][col] = elements[index]
            index += 1

        row = n - i - 1
        for col in range(n - i - 2, i - 1, -1):
            # print(row, col, index)
            A[row][col] = elements[index]
            index += 1

        # print(A)
        # print(index)

        col = i
        for row in range(n - i - 2, i, -1):
            # print(row, col, index)
            A[row][col] = elements[index]
            index += 1

        # print(A)
        # print(row)
        # print(col)
        i += 1

    return A

res = solve(5)
print(res)
