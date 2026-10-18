# Given a string A consisting of lowercase characters.
# Check if characters of the given string can be rearranged to form a palindrome.
# Return 1 if it is possible to rearrange the characters of the string A
# such that it becomes a palindrome else return 0.
# Input Format
# First argument is an string A.
# Output Format
# Return 1 if it is possible to rearrange the characters of the string A
# such that it becomes a palindrome else return 0.
# A = "abcde"
# O/P: 0

def solve(A):
    n = len(A)
    hashmap = {}

    for i in range(n):
        if hashmap.get(A[i], 0):
            hashmap[A[i]] += 1
        else:
            hashmap[A[i]] = 1

    print(hashmap)
    size = len(hashmap)
    count = 0
    odd_count = 0
    for key in hashmap.keys():
        if hashmap[key] % 2 == 0:
            count += 1
        elif hashmap[key] % 2 == 1 and odd_count == 0:
            odd_count = 1
        else:
            return 0

    if count == size - 1 or count == size:
        return 1

    return 0

res = solve("inttnikjmjbemrberk")
print(res)