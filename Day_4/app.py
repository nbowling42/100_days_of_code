import random

while True:
    rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

    paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

    scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
    graphics = [rock, paper, scissors]

    player_choice = int(input("What do you choose? Type 1 for Rock, 2 for Paper, or 3 for Scissors: "))
    computer_choice = random.randint(1, 3)

    if player_choice < 1 or player_choice > 3:
        print("Invalid choice. Please choose 1, 2, or 3.")
        continue  

    print(graphics[player_choice-1])
    print("Computer chose: ")
    print(graphics[computer_choice-1])

    if player_choice == computer_choice:
        print("It's a draw!")
    elif player_choice == 1 and computer_choice == 3:
        print("You win!")
    elif player_choice == 2 and computer_choice == 1:
        print("You win!")
    elif player_choice == 3 and computer_choice == 2:
        print("You win!")
    else:
        print("You lose :(")

    play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
    if play_again != 'y':
        break
