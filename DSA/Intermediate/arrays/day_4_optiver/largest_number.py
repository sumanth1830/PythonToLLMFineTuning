# Given an array A of non-negative integers, arrange them such that they form the largest number.
# Note: The result may be very large, so you need to return a string instead of an integer.
# Input Format
# The first argument is an array of integers.
# Output Format
# Return a string representing the largest number.
# A = [3, 30, 34, 5, 9]
# O/P: "9534330"
from functools import cmp_to_key


def solve(A):
    def cmp_func(x, y):
        if x + y > y + x:
            return 1
        elif x == y:
            return 0
        else:
            return -1

    nums = [str(num) for num in A]
    nums.sort(key=cmp_to_key(cmp_func), reverse=True)
    if nums[0] == '0':
        return '0'
    return ''.join(nums)


res = solve([3, 30, 34, 5, 9])
print(res)