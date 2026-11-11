# WORK OF AIRBUSFAN501. I MADE THIS AND WROTE ALL THE CODE MYSELF

import random

print("My number guessing game")
print()

while True: 
    correct_number = random.randint(1, 100)

    while True:
        answer = int(input("Guess a number beetween 1 and 100:"))

        if answer ==  correct_number:
            print("You guessed the correct number!")
            break

        elif answer != correct_number: 
            print("Wrong number! Try again.")

    play_again = input("\nDo you want to play again? (write 'yes' or 'no'): ")
    if play_again.lower() != "yes":
        print("Thank you for playing the game!")
        break