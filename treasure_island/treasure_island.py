def treasure_island():
    print("""
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
""")
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.\n")

    choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right":\n').lower()
    if choice1 != "left":
        print("You fell into a hole. Game Over.")
        return

    choice2 = input('You\'ve come to a lake. Type "wait" to wait for a boat or "swim" to swim across:\n').lower()
    if choice2 != "wait":
        print("You get attacked by an angry trout. Game Over.")
        return

    choice3 = input(
        "You arrive at the island unharmed.\n"
        "There is a house with 3 doors: red, yellow, and blue.\n"
        "Which colour do you choose?\n"
    ).lower()

    if choice3 == "red":
        print("It's a room full of fire. Game Over.")
    elif choice3 == "blue":
        print("You enter a room of beasts. Game Over.")
    elif choice3 == "yellow":
        print("You found the treasure! 🏆 You Win!")
    else:
        print("You chose a door that doesn't exist. Game Over.")


while True:
    treasure_island()
    again = input("\nDo you want to play again? Type 'yes' or 'no': ").lower()
    if again != "yes":
        print("Thanks for playing! 👋")
        break
