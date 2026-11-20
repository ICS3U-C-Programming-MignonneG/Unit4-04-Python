#!/usr/bin/python3
# Created by: Mignonne Gihozo
# Created on: 2026-11-17
# This program asks the user to guess a random number until they get it right.

import random


def main():
    # This function generates a random number and loops until guessed.
    correct_number = random.randint(0, 9)

    while True:
        try:
            # Input
            user_input = input("Guess a number between 0 and 9: ")
            user_guess = int(user_input)

            if user_guess < 0 or user_guess > 9:
                print("Please enter a positive number between 0 and 9.")
            elif user_guess == correct_number:
                print(f"{user_guess} was guessed correctly!")
                break
            else:
                print(f"{user_guess} was guessed incorrectly. Please try again.")
        except ValueError:
            print(f"{user_input} is not a valid number.")


if __name__ == "__main__":
    main()
