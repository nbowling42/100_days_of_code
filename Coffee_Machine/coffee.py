from menu import MENU, resources, coins

#functions
def report():
    """Prints a report of all of the current resources in the machine"""
    for key in resources:
        print(f"{key}: {resources[key]}")
    print(f"Money: {bank}")

def check_resources(order):
    """Returns True if there are enough resources to make the order, otherwise it will return False"""
    for key in order["ingredients"]:
        if order["ingredients"][key] > resources[key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True

def process_coins():
    """Ask the user to insert coins and then calculates and returns the total value"""
    print("Please insert coins.")
    total = 0
    for key in coins:
        coin = int(input(f"How many {key}?: "))
        total += (coin * coins[key])
    return total

def check_transaction(money, cost):
    """Returns True along with any change if enough money was inserted, otherwise it will return False"""
    if money < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = money - cost
        if change > 0:
            print(f"Here is ${change:.2f} dollars in change.")
            return change
        return True

def make_coffee(coffee, order):
    """Makes the coffee and subtracts the resources from the machine"""
    for key in order["ingredients"]: 
        resources[key] -= order["ingredients"][key]
    print(f"Here is your {coffee}. Enjoy!")

bank = 0

while True:
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

    #Prints a report of the current reources in the machine
    if prompt == 'report':
        report()
    #Turns the machine off    
    elif prompt == 'off':
        break
    else:
        #Checks if there are enough resources to make the coffee
        if check_resources(MENU[prompt]):
            #Collects money from the user
            money = process_coins()
            #Checks if the user inserted enough money
            if check_transaction(money, MENU[prompt]["cost"]):
                #Adds money to the machines bank and makes the coffee
                bank += MENU[prompt]["cost"]
                make_coffee(prompt, MENU[prompt])
