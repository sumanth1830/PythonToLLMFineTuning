# Alex and Sam are good friends. Alex is doing a lot of programming these days.
# He has set a target score of A for himself.
# Initially, Alex's score was zero. Alex can double his score by doing a question,
# or Alex can seek help from Sam for doing questions that will contribute 1 to Alex's score. Alex wants his score to be precisely A. Also, he does not want to take much help from Sam.
#
# Find and return the minimum number of times Alex needs to take help from
# Sam to achieve a score of A.
# Input Format
# The only argument given is an integer A.
#
# Output Format
# Return the minimum number of times help taken from Sam.
# A = 5
# 2

def solve(A):
    # Observation
    # Score doubles -> * 2
    # or help from sam -> + 1
    # doubling can be done with left shift
    # Help can be coded by setting LSB
    # Find difference between current score and A
    # double or add accordingly

    # New Obs
    # We need not double answer by lshift
    # As we need to track only help from Sam
    # So we rshift -> divide by 2
    ans = 0
    while ans <= A:
        if A & 1 == 1:
            # if A is odd, we add 1
            ans += 1
        A >>= 1

    return ans



res = solve(5)
print(res)