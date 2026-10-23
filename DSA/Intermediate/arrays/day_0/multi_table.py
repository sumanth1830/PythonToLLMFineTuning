"""
Problem Description
Take a number A as input, print its multiplication table having the first 10 multiples.

Problem Constraints
1 <= A <= 1000


Input Format
First line contains a single integer A.

Output Format
Print 10 lines, ith line containing ith multiple.
"""

def main():
    A = int(input())
    for i in range(1, 11):
        print(f" {A} * {i} = {A * i}")


if __name__ == "__main__":
    main()
