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

def ace_check(hand):
    while sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)

#game logic
def blackjack(deck):

    #deal the initial hands and check for aces
    player_hand = [choose_card(deck) for card in range(2)]
    computer_hand = [choose_card(deck) for card in range(2)]
    ace_check(player_hand)
    ace_check(computer_hand)

    #players turn, break once they pass
    while True:
        #show the hands and ask if the player wants to hit or pass
        print(f"    Your Cards: {player_hand}, current score: {sum(player_hand)}")
        print(f"    Computer's first card: {computer_hand[0]}")

        hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if hit == 'y':
            player_hand.append(choose_card(deck))
            ace_check(player_hand)
            if sum(player_hand) > 21:
                print(f"    Your Cards: {player_hand}, final score: {sum(player_hand)}")
                print("    You went over 21. You lose!")
                return False
        else:
            break

    #computers turn, breaks once it is >= the sum of player_hand
    while sum(computer_hand) < sum(player_hand) or sum(computer_hand) < 17:
        computer_hand.append(choose_card(deck))
        ace_check(computer_hand)

    #compare the hands and print the results
    print(f"    Your final hand: {player_hand}, final score: {sum(player_hand)}")
    print(f"    Computer's final hand: {computer_hand}, final score: {sum(computer_hand)}")
    compare_hands(player_hand, computer_hand)

#deck of cards (unlimited)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
#start the game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    print(logo)
    blackjack(cards)
