# Problem Description
# Give a N * N square matrix A, return an array of its anti-diagonals.
# Look at the example for more details.
#
# Problem Constraints
# 1<= N <= 1000
# 1<= A[i][j] <= 1e9
# Input Format
# Only argument is a 2D array A of size N * N.
#
# Output Format
# Return a 2D integer array of size (2 * N-1) * N, representing the anti-diagonals of input array A.
# The vacant spaces in the grid should be assigned to 0

# Approach
# Obs:
# Find the anti diagonals
# Save them as lists
# Loop over this list of lists and append zeros if their len < n

def solve(A):
    n = len(A)
    anti_diagonals_list = []

    for col in range(0, n):
        # Loop from start of the col to the end
        # For each col, start with first element
        # And then go anti diagonally by row + 1, col - 1
        # We will miss out on the diagonals spanning from other rows
        i = 0
        j = col
        diagonal = []
        while i <= col and j >= 0:
            diagonal.append(A[i][j])
            i += 1
            j -= 1
        anti_diagonals_list.append(diagonal)

    for i in range(1, n):
        # Here we know that we need to handle diagonals from rows other than 0
        # So we start from row 1
        # But these diagonals would be spanning from last col so j = n - 1
        # Then by the same logic row + 1, col - 1, we find the complete diagonal
        j = n - 1
        row = i
        diagonal = []
        while row < n:
            diagonal.append(A[row][j])
            row += 1
            j -= 1

        anti_diagonals_list.append(diagonal)

    for diagonal in anti_diagonals_list:
        # Traversing over each anti-diagonal and filling in zeros to match the required o/p
        if len(diagonal) < n:
            for i in range(n - len(diagonal)):
                diagonal.append(0)

    # print(anti_diagonals_list)
    return anti_diagonals_list



res = solve([[1 ,2, 3], [4, 5, 6], [7, 8, 9]])
print(res)