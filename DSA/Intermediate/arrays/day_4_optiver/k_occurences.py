# Groot has N trees lined up in front of him where
# the height of the i'th tree is denoted by H[i].
# He wants to select some trees to replace his broken branches.
# But he wants uniformity in his selection of trees.
# So he picks only those trees whose heights have frequency B.
# He then sums up the heights that occur B times.
# (He adds the height only once to the sum and not B times).
# But the sum he ended up getting was huge so he prints it modulo 10^9+7.
# In case no such cluster exists, Groot becomes sad and prints -1.
# N=5 ,B=2 ,C=[1 2 2 3 3]
# O/P: 5
# There are 3 distinct numbers in the array which are 1,2,3.
# Out of these, only 2 and 3 occur twice. Therefore the answer is sum of 2 and 3 which is 5.

def solve(N, B, C):
    A = {}
    val = 0
    flag = False
    for i in range(N):
        if C[i] in A:
            A[C[i]] += 1
        else:
            A[C[i]] = 1


    for key in A.keys():
        if A[key] == B:
            flag = True
            val += key

    if flag:
        return val % 1000000007

    return -1


# res = solve(N=5 ,B=2 ,C=[1, 2, 2, 3, 3])
res = solve(3, 2, [0, 0, 1])
print(res)