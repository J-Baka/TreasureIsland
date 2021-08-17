
print("Welcome to Treasure Island. Your mission is to find the treasure.")

choice1 = input("You are at a crossroads. Would you like to go left or right?\n")
if choice1 == "left":
    choice2 = input("There is a lake before you. Would you like to swim or wait?\n")
    if choice2 == "wait":
        choice3 = input("You wait until night and the moonlight illuminates an invisible bridge. "
                        "On the other side there are three doors.\n"
                        "Which door would you like to enter? red, blue, or yellow?\n")
        if choice3 == "red":
            print("There is an apple on a pedestal. You consume it and find it to be poisoned. Game Over")
        elif choice3 == "yellow":
            print("Congratulations!! You found the treasure!")
        else:
            print("You walk in on a trio of trolls enjoying dinner and you've just been added to the menu. Game Over")
    else:
        print("Oh no, the lake is filled with crocodiles! Game Over")
else:
    print("You have walked off a cliff. Game Over")
