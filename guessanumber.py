# guessanumber.py
# number guesser game
# S.Winter.C.
# created: 10.21.2024
# last updated: 10.21.2024

import random


def guesser():
    session = True
    while session:
        playing = 1
        wins = 2
        won = False
        while playing == 1:
            real_num = random.randint(1, (1 * (10 ** wins)))

            while True:
                try:
                    first_guess = int(input(f"Guess a number from 1 to {1 * ( 10 ** wins)}!"))
                    break
                except ValueError:
                    print("Error: Not a number.")

            if first_guess == real_num:
                print("You win!")
                wins += 1

            elif first_guess > real_num or first_guess < real_num:
                guess_list = [first_guess]
                x = 8

                while x > 0 and not won:

                    while True:
                        try:
                            guess = int(input(f"You have {x} guesses remaining. Please make a guess."))
                            break
                        except ValueError:
                            print(f"I might kill myself tonight")

                    guess_list.append(guess)

                    dif_last = abs((real_num - guess_list[len(guess_list) - 2]))
                    dif_current = abs((real_num - guess_list[len(guess_list) - 1]))

                    if guess_list[len(guess_list) - 1] == real_num:
                        print("You Win!")
                        wins += 1
                        won = True

                    elif dif_last > dif_current:
                        print("Warmer..")

                    elif dif_last < dif_current:
                        print("Colder..")

                    x = x-1

                if x == 0:
                    print(f"You lose. The number was {real_num}.")
        ending = True
        while ending:
            try:
                end = input(f"Would you like to continue?\n"
                            f"Input 1 to continue playing.\n"
                            f"Input 2 to end session.")
                if end == 1:
                    ending = False
                elif end == 2:
                    session = False
                    ending = True
                else:
                    print(f"You must input 1 or 2.")
            except ValueError:
                print(f"Improper input.")


guesser()
