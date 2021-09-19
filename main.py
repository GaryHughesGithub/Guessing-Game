#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

print(logo)

print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")

difficulty = input("Choose a difficulty level. Type 'easy' or 'hard': ")

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
elif not difficulty == "easy" or "hard":
    print("Invalid selection, please stop and restart the game.")

answer = random.randint(1,100)

correct_guess = False

while correct_guess == False:

    if attempts <= 0:
        print("Sorry you lose, you have no lives left!")
        break

    print(f"You have {attempts} attempts remaining to guess the number.")
    # print(f"pssst the answer is {answer}!")

    guess = int(input("Make a guess: "))

    if guess > answer:
        print("Too High")
        attempts -= 1
    elif guess < answer:
        print("Too Low")
        attempts -= 1
    elif guess == answer:
        print("Thats correct well done!")
        correct_guess = True

