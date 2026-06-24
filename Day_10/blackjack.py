import random
from art import logo

#functions
def choose_card(deck):
    return random.choice(deck)

def compare_hands(hand1, hand2):
    if sum(hand2) <= 21:
        if sum(hand1) == sum(hand2):
            print("It's a draw!")
        elif sum(hand1) > sum(hand2):
            print("You win!")
        else:
            print("You lose!")
    else:
        print("You win!")

#deck of cards (unlimited)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#the game of blackjack
def blackjack():

    #deal the initial hands
    player_hand = [choose_card(cards) for card in range(2)]
    computer_hand = [choose_card(cards)]

    #players turn, break once they pass
    while True:
        #show the hands and ask if the player wants to hit or pass
        print(f"    Your Cards: {player_hand}, current score: {sum(player_hand)}")
        print(f"    Computer's first card: {computer_hand[0]}")

        hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if hit == 'y':
            player_hand.append(choose_card(cards))
            if sum(player_hand) > 21:
                print(f"    Your Cards: {player_hand}, final score: {sum(player_hand)}")
                print("    You went over 21. You lose!")
                return False
        else:
            break

    #computers turn, breaks once it is >= the sum of player_hand
    computer_hand.append(choose_card(cards))
    while sum(computer_hand) < sum(player_hand):
        computer_hand.append(choose_card(cards))

    #compare the hands and print the results
    print(f"    Your final hand: {player_hand}, final score: {sum(player_hand)}")
    print(f"    Computer's final hand: {computer_hand}, final score: {sum(computer_hand)}")
    compare_hands(player_hand, computer_hand)
    
#start the game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    print(logo)
    blackjack()
