"""
Problem Description
You are given an integer N you need to print all the Armstrong Numbers between 1 to N. (N inclusive).

If sum of cubes of each digit of the number is equal to the number itself, then the number is called an Armstrong number.
For example, 153 = ( 1 * 1 * 1 ) + ( 5 * 5 * 5 ) + ( 3 * 3 * 3 ).
Note: All the test cases in this problem are limited to 3 digit numbers.

Problem Constraints
1 <= N <= 500

Input Format
First and only line of input contains an integer N.

Output Format
Output all the Armstrong numbers in range [1,N] each in a new line.

"""

def main():
    N = int(input())
    for i in range(1, N):
        ams_sum = 0
        temp = i
        while temp > 0:
            digit = temp % 10
            ams_sum += digit ** 3
            temp //= 10

        if ams_sum == i:
            print(i)

if __name__ == "__main__":
    main()
