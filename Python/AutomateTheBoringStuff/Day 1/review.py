# Chapters 1, 2 and 3
# Ask the user for a whole number n.
# Loop from 1 to n and print how many of those numbers are even and how many are odd.

# number = int(input("Enter a number: "))
# even_count = 0
# odd_count = 0
# for i in range(1, number + 1):
#     if i % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
#
# print(f"Even : {even_count}, Odd : {odd_count}")

# Medium: FizzBuzz with a twist
# Ask the user for a number n and print 1 to n, with these replacements:
#
# Multiples of 3 print Fizz.
# Multiples of 5 print Buzz.
# Multiples of both print FizzBuzz.
# Twist: any number containing the digit 7 prints Boom, and that rule beats all the others.

# number = int(input("Enter a number: "))
# for i in range(1, number + 1):
#     if '7' in str(i):
#         print("Boom")
#         continue
#
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


# Hard: Number guessing game with validation
#
# The computer picks a random number from 1 to 100.
# The player gets at most 7 guesses. After each one, print Too high or Too low.
# If the player types something that isn’t a number, say so and don’t count it as a guess.
# Use .isdecimal().
# Typing quit ends the game immediately with sys.exit().
# If the player wins, print how many guesses they took. If they run out, reveal the number.
# Finally, ask Play again? (y/n) and restart if they answer y. You’ll need an outer loop for this.

import random
import sys


play_game = True

while play_game:
    won = False
    target_number = random.randint(1, 100)
    guesses = 0
    while guesses < 7:
        number = input("Guess the number: ").strip()

        if number.lower() == "quit":
            sys.exit()

        if number.isdecimal():
            number = int(number)
            guesses += 1
            if number < target_number:
                print("You prediction was lower!")
            elif number > target_number:
                print("Your prediction was high!")
            else:
                print("You are on spot!")
                print(f"You predicted in {guesses} guesses.")
                won = True
                break
        else:
            print("Enter a number!")


    if not won:
        print("You exhausted your guesses!")
        print("The number is", target_number)
    val = input("Do you want to play again? (y/n)")

    play_game = val.lower() == "y"