import random
from random import randint

print("Welcome to the number guessing game!")
the_seed_value = input("Enter random seed: ")
random.seed(the_seed_value)

play = str("yes")
while play == "yes":
    num = randint(1, 100)
    guess = 0
    round = 0
    #print(num)
    while num!=guess:
        #print(num)
        #print(guess)
        guess = int(input("\nPlease enter a guess: "))
        round += 1
        if guess>num:
            print("Lower")
        elif guess<num:
            print("Higher")
        else:
            print("Congratulations. You guessed it!\nIt took you " + str(round) + " guesses.\n")
            break
    play = str(input("Would you like to play again (yes/no)? "))
    if play == "no":
        print("Thank you. Goodbye.")
        break

