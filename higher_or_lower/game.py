from random import choice
from art import logo, vs
from game_data import data

#functions
def get_random_user():
    """Get data of a random user from the data list."""
    return choice(data)

def check_answer(guess, user1_followers, user2_followers):
    """Check if the user's guess is correct."""
    if user1_followers > user2_followers:
        return guess == 'a'
    else:
        return guess == 'b'
    
def clear_terminal():
    """clear the terminal"""
    print("\033[H\033[J", end="")

def play_game(highscore):
    #clear terminal at the start
    clear_terminal()

    #set the initial score
    score = 0

    #print logo and get initial users to compare
    print(logo)
    user1 = get_random_user()
    user2 = get_random_user()
    #make sure the users are not the same
    while user1 == user2:
        user2 = get_random_user()
    
    while True:
        #list the users to compare and show the high score
        print(f"Highscore: {highscore}")
        print(f"Compare A: {user1['name']}, a {user1['description']}, from {user1['country']}.")
        print(vs)
        print(f"Against B: {user2['name']}, a {user2['description']}, from {user2['country']}.")
        
        #ask the user for their guess and then check if the guess is right or wrong
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        #if the guess is correct we add 1 to the score, make user2 the new user1, and then get a new user2
        if check_answer(guess, user1['follower_count'], user2['follower_count']):
            score += 1
            user1 = user2
            while user2 == user1:
                user2 = get_random_user()
            #clear the terminal and reprint the logo
            clear_terminal()
            print(logo)
            print(f"You're right! Current score: {score}")
        #if they guess wrong check if they got a new high score and exit the game
        else:
            print(f"\nSorry, that's wrong. Final score: {score}")
            if score > highscore:
                highscore = score
                print(f"New high score! {highscore}")
            return highscore

#start the game - keeps track of high score for only 1 session before resetting to 0
highscore = play_game(0)
while input("Do you want to play again? (y/n): ").lower() == 'y':
    highscore = play_game(highscore)
