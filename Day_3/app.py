import sys

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure. \n")

print("You come across a fork in the road. Which way do you go?")
while True:
    choice1 = input('  Type "Left" or "Right": ').lower()

    if choice1 == "right":
        print("\nYou fell into a deep hole. Game over.")
        sys.exit()
    elif choice1 == "left":
        break
    else:
        print("\nPlease type either 'Left' or 'Right'.")

print("\nYou come across a huge lake with an island in the middle. What do you do?")
while True:
    choice2 = input('Type "Swim" to swim across or "Wait" to wait for a boat: ').lower()
    if choice2 == "swim":
        print("\nYou got attacked by an angry trout! Game over.")
        sys.exit()
    if choice2 == "wait":
        break
    else:
        print('\nPlease type either "Swim" or "Wait".')

print("\nThe boat takes you to the island where you find 3 doors waiting to be opened.")
while True:
    choice3 = input('Which door will you unlock? Type "Red", "Blue", or "Yellow": ').lower()
    if choice3 == "red":
        print("\nIt's a room full of fire. Game over.")
        sys.exit()
    elif choice3 == "blue":
        print("\nYou enter a room full of beast. Game over.")
        sys.exit()
    elif choice3 == "yellow":
        print("\nYou found the treasure! You Win!")
        break
    else:
        print('\nPlease type either "Red", "Blue" or "Yellow".')
