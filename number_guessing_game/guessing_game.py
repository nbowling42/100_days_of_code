from art import logo
import random

#functions
def check_guess(num, answer):
    if num > answer:
        print("Too high.")
    elif num < answer:
        print("Too low.")
    else:
        print(f"You got it! The answer was {answer}.")
        return True

game_over = False
while not game_over:
    #print the logo and welcome message
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    #choose a random number between 1 and 100 and set the number of attempts based on difficulty level
    number = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    else:
        print("Invalid difficulty level. Please choose 'easy' or 'hard'.")

    #game loop
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts -= 1
        if check_guess(guess, number):
            game_over = True
            break

    #if the player runs out of attempts, print a losing message
    if attempts == 0:
        print("You've run out of guesses, you lose.")
        
    #ask the player if they want to play again
    play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
    if play_again == 'n':
        game_over = True
