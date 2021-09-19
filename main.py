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
        print(f"Sorry you lose, you have {attempts} lives left! The correct number was {answer}")
        break

    print(f"You have {attempts} attempts remaining to guess the number.")
    print(f"pssst the answer is {answer}!")

    guess = int(input("Make a guess: "))

    if guess > answer:
        print("Too High")
        attempts -= 1
    elif guess < answer:
        print("Too Low")
        attempts -= 1
    elif guess == answer:
        print(f"Thats correct! the answer was {answer} well done!")
        correct_guess = True

