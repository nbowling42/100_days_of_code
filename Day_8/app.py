from art import logo

def find_highest_bidder(bids_dict):
    highest_bid = 0
    winner = ""
    for key in bids_dict:
        if bids_dict[key] > highest_bid:
            highest_bid = bids_dict[key]
            winner = key
    print('\n' * 20)
    print(f"The winner is {winner}, with a bid of ${highest_bid:.2f}")

print(logo)
print("Welcome to the Secret Auction.")

bids = {}
continue_auction = True

while continue_auction:
    name = input("What is your name?: ")
    price = float(input("What is your bid?: $"))
    bids[name] = price

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': \n").lower()
    if more_bidders == 'yes':
        print('\n' * 20)
    elif more_bidders == 'no':
        find_highest_bidder(bids)
        continue_auction = False
