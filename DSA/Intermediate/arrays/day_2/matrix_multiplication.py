# You are given two integer matrices A(having M X N size) and B(having N X P).
# You have to multiply matrix A with B and return the resultant matrix. (i.e. return the matrix AB).
# Input Format
#
# The first argument given is the 2-D integer matrix A.
# The second argument given is the 2-D integer matrix B.
# Output Format
#
# Return a 2D integer matrix denoting AB.
# A = [[1, 2],
#      [3, 4]]
# B = [[5, 6],
#      [7, 8]]

def solve(A, B):
    m = len(A) # m * n
    n = len(A[0]) # n * p
    p = len(B[0])
    C = [[0] * p for _ in range(m)] # m * p

    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C


res = solve(
[[1, 2],
     [3, 4]],
[[5, 6],
     [7, 8]]
)
print(res)