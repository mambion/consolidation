import random

# Define global variables for dice
dice1 = 0
dice2 = 0
dice3 = 0

# Create the function for the intial dice rolls
def random_roll():
    global dice1, dice2, dice3
    input("Hit 'enter' to roll dice 1.") 
    dice1 = random.choice([1, 2, 3, 4, 5, 6])
    print("Dice 1:", dice1)
    input("Hit 'enter' to roll dice 2.")
    dice2 = random.choice([1, 2, 3, 4, 5, 6])
    print("Dice 2:", dice2)
    input("Hit 'enter' to roll dice 3.")
    dice3 = random.choice([1, 2, 3, 4, 5, 6])
    print("Dice 3:", dice3)

# improved for class
def random_roll():
    "returns a list of three random numbers between 1 and 6"
    input("Hit 'enter' to roll dice 1.") 
    dice1 = random.choice([1, 2, 3, 4, 5, 6])
    print("Dice 1:", dice1)
    input("Hit 'enter' to roll dice 2.")
    dice2 = random.choice([1, 2, 3, 4, 5, 6])
    print("Dice 2:", dice2)
    input("Hit 'enter' to roll dice 3.")
    dice3 = random.choice([1, 2, 3, 4, 5, 6])
    print("Dice 3:", dice3)
    all_dice = [dice1, dice2, dice3]
    return all_dice
## tests
# result = random_roll()
# print(result)

# Create the function to check for matching dice
def check_matches(dice):
    dice1, dice2, dice3 
    if dice1 == dice2 == dice3:
        print("Oh no!")
    else:
        if dice1 == dice2:
            print("Dice 1 and Dice 2 are locked.")
        if dice1 == dice3:
            print("Dice 1 and Dice 3 are locked.")
        if dice2 == dice3:
            print("Dice 2 and Dice 3 are locked.")
        total = [dice1, dice2, dice3]
        print("Your current total is", sum(total), "| Dice 1:", dice1, "Dice 2:", dice2, "Dice 3:", dice3)

# Create the function to check for matching dice AFTER the user has
# chosen to re-roll
def check_reroll():
    global dice1, dice2, dice3
    if dice1 == dice2 == dice3:
        print("You have tupled out this round!")

# Create the function to re-roll when all dice are different
def unlocked_reroll():
    global dice1, dice2, dice3
    re_roll = None
    choice = input("Would you like to re-roll one of the dice? (y/n) ")
    if choice.lower() == "y" and dice1 != dice2 and dice1 != dice3 and dice2 != dice3:
        re_roll = input("Which dice do you want to re-roll? (1, 2, or 3) ")
        if re_roll == "1":
            input("Press 'enter' to re-roll dice 1.")
            dice1 = random.choice([1, 2, 3, 4, 5, 6])
            print("New dice 1:", dice1)
            print(totals())
        elif re_roll == "2":
            input("Press 'enter' to re-roll dice 2.")
            dice2 = random.choice([1, 2, 3, 4, 5, 6])
            print("New dice 2:", dice2)
            print(totals())
        elif re_roll == "3":
            input("Press 'enter' to re-roll dice 3.")
            dice3 = random.choice([1, 2, 3, 4, 5, 6])
            print("New dice 3:", dice3)
            print(totals())
    else:
        print("You have chosen to stand with your current total.")

# dice1 = 1
# dice2 = 6
# dice3 = 6

# The function that tells the user which dice they can roll when
# they have a matching pair of dice
def locked_reroll():
    global dice1, dice2, dice3
    locked_choice = input("Would you like to re-roll the unlocked dice? (y/n) ")
    if locked_choice.lower() == "y":
        if dice1 != dice2 and dice1 != dice3 and dice2 == dice3:
            print("You can only re-roll Dice 1.")
            input("Press 'enter' to re-roll dice 1.")
            dice1 = random.choice([1, 2, 3, 4, 5, 6])
            print("New dice 1:", dice1)
            print(totals())
        elif dice1 != dice2 and dice1 == dice3 and dice2 != dice3:
            print("You can only re-roll Dice 2.")
            input("Press 'enter' to re-roll dice 2.")
            dice2 = random.choice([1, 2, 3, 4, 5, 6])
            print("New dice 2:", dice2)
            print(totals())
        elif dice1 == dice2 and dice1 != dice3 and dice2 != dice3:
            print("You can only re-roll Dice 3.")
            input("Press 'enter' to re-roll dice 3.")
            dice3 = random.choice([1, 2, 3, 4, 5, 6])
            print("New dice 3:", dice3)
            print(totals())
        else:
            print("You have chosen to stand with your current total.")
            print(totals())



# Function that displays totals
def totals():
    if dice1 == dice2 == dice3:
        input("Press 'enter' to continue")
    else:
        total = [dice1, dice2, dice3]
        print("Your total for the round is", sum(total), "| Dice 1:", dice1, "Dice 2:", dice2, "Dice 3:", dice3)

# # Ask to re-roll with locked dice
# if dice1 != dice2 and dice1 != dice3 and dice2 == dice3:
#     locked_reroll()
# elif dice1 != dice2 and dice1 == dice3 and dice2 != dice3:
#     locked_reroll()
# elif dice1 == dice2 and dice1 != dice3 and dice2 != dice3:
#     locked_reroll()

# # Ask to re-roll with unlocked dice
# if dice1 != dice2 and dice1 != dice3 and dice2 != dice3:
#     unlocked_reroll()


# Print totals
# totals()

# Create the function for the main game
# Start the game and display rolls
print("Welcome to Tuple Out! Click 'enter' to see the rules of the game:")
print("1. You and another friend wil have 3 dice each.")
input()
print("2. You each roll the three dice once.")
input()
print("3. If you get low numbers, you will have the chance to re-roll one of the dice.")
input()
print("""4. However, if you roll the same number twice, those dice will lock and you won't be able to re-roll them. And if you roll the same number 3 times, you will not get any points for the round.""")
input()
print("""5. You and your friend will play 5 rounds and whoever has the most points at the end of the 5 rounds wins the game.""")
input("Press enter to play!")

total_score = 0
for round_number in range(1, 6):
    print(f"\n--- Round {round_number} ---")
    dice_results = random_roll()
    check_matches(dice_results)

    if dice1 != dice2 and dice1 != dice3 and dice2 == dice3:
        locked_reroll()
    elif dice1 != dice2 and dice1 == dice3 and dice2 != dice3:
        locked_reroll()
    elif dice1 == dice2 and dice1 != dice3 and dice2 != dice3:
        locked_reroll()

    check_reroll()

    if dice1 != dice2 and dice1 != dice3 and dice2 != dice3:
        unlocked_reroll()
    
    if dice1 == dice2 == dice3:
        print("No points will be added.")
    else:
        total_score += sum([dice1, dice2, dice3])
        print(f"Total score after round {round_number}: {total_score}")

print(f"\nGame Over! Your final score after 5 rounds is: {total_score}")
