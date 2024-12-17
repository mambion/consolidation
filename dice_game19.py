import random

# Create the function for the initial dice rolls
def random_roll():
    "the first random roll for the game"
    input("Hit 'enter' to roll dice 1.") 
    dice1 = random.choice([1, 2, 3, 4, 5, 6])
    print("Dice 1:", dice1)
    input("Hit 'enter' to roll dice 2.")
    dice2 = random.choice([1, 2, 3, 4, 5, 6])
    print("Dice 2:", dice2)
    input("Hit 'enter' to roll dice 3.")
    dice3 = random.choice([1, 2, 3, 4, 5, 6])
    print("Dice 3:", dice3)
    return dice1, dice2, dice3

# Create the function to check for matching dice
def check_matches(all_dice):
    "checks for matching dice"
    dice1, dice2, dice3 = all_dice
    if dice1 == dice2 == dice3:
        print("Oh no! You have tupled out!")
        return True  # Indicates that the player has "tupled out"
    else:
        if dice1 == dice2:
            print("Dice 1 and Dice 2 are locked.")
        if dice1 == dice3:
            print("Dice 1 and Dice 3 are locked.")
        if dice2 == dice3:
            print("Dice 2 and Dice 3 are locked.")
        total = sum(all_dice)
        print("Your current total is", total, "| Dice 1:", dice1, "Dice 2:", dice2, "Dice 3:", dice3)
        return False  # Indicates that the player can continue

# Create the function to check for matching dice AFTER the user has chosen to re-roll
def check_reroll(all_dice):
    "checks for matching dice after re-rolling"
    dice1, dice2, dice3 = all_dice
    if dice1 == dice2 == dice3:
        print("You have tupled out this round!")
        return True
    return False

# Create the function to re-roll when all dice are different
def unlocked_reroll(all_dice):
    "asks which dice to re-roll when all dice are different"
    dice1, dice2, dice3 = all_dice
    re_roll = None
    choice = input("Would you like to re-roll one of the dice? (y/n) ")
    if choice.lower() == "y" and dice1 != dice2 and dice1 != dice3 and dice2 != dice3:
        re_roll = input("Which dice do you want to re-roll? (1, 2, or 3) ")
        if re_roll == "1":
            input("Press 'enter' to re-roll dice 1.")
            dice1 = random.choice([1, 2, 3, 4, 5, 6])
            print("New dice 1:", dice1)
        elif re_roll == "2":
            input("Press 'enter' to re-roll dice 2.")
            dice2 = random.choice([1, 2, 3, 4, 5, 6])
            print("New dice 2:", dice2)
        elif re_roll == "3":
            input("Press 'enter' to re-roll dice 3.")
            dice3 = random.choice([1, 2, 3, 4, 5, 6])
            print("New dice 3:", dice3)
    else:
        print("You have chosen to stand with your current total.")
    return dice1, dice2, dice3

def locked_reroll(all_dice):
    "asks which dice to re-roll when two dice are locked"
    dice1, dice2, dice3 = all_dice
    choice = input("Would you like to re-roll the unlocked dice? (y/n) ")
    if choice.lower() == "y":
        if dice1 != dice2 and dice1 != dice3 and dice2 == dice3:
            print("You can only re-roll Dice 1.")
            input("Press 'enter' to re-roll dice 1.")
            dice1 = random.choice([1, 2, 3, 4, 5, 6])
            print("New dice 1:", dice1)
            print(totals(dice1, dice2, dice3))
        elif dice1 != dice2 and dice1 == dice3 and dice2 != dice3:
            print("You can only re-roll Dice 2.")
            input("Press 'enter' to re-roll dice 2.")
            dice2 = random.choice([1, 2, 3, 4, 5, 6])
            print("New dice 2:", dice2)
            print(totals(dice1, dice2, dice3))
        elif dice1 == dice2 and dice1 != dice3 and dice2 != dice3:
            print("You can only re-roll Dice 3.")
            input("Press 'enter' to re-roll dice 3.")
            dice3 = random.choice([1, 2, 3, 4, 5, 6])
            print("New dice 3:", dice3)
            print(totals(dice1, dice2, dice3))
    else:
        print("You have chosen to stand with your current total.")
    return dice1, dice2, dice3

def totals(dice1, dice2, dice3):
    "prints the total or continues the game"
    if dice1 == dice2 == dice3:
        input("Press 'enter' to continue")
    else:
        total = [dice1, dice2, dice3]
        print("Your total for the round is", sum(total), "| Dice 1:", dice1, "Dice 2:", dice2, "Dice 3:", dice3)

# Rules for the game
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

# Run the game!
total_score = 0
for round_number in range(1, 6):
    print(f"\n--- Round {round_number} ---")
    dice_results = random_roll()
    dice1, dice2, dice3 = dice_results  # Unpack the results

    if check_matches(dice_results):
        print("No points will be added.")
        continue  # Skip to the next round if all dice match

    # Check for locked re-rolls
    if (dice1 != dice2 and dice1 != dice3 and dice2 == dice3) or \
        (dice1 != dice2 and dice1 == dice3 and dice2 != dice3) or \
        (dice1 == dice2 and dice1 != dice3 and dice2 != dice3):
        dice_results = locked_reroll(dice_results)

    # Check for unlocked re-rolls
    if dice1 != dice2 and dice1 != dice3 and dice2 != dice3:
        dice_results = unlocked_reroll(dice_results)

    # Calculate total score for the round
    if dice1 == dice2 == dice3:
        print("No points will be added.")
    else:
        total_score += sum(dice_results)
        print(f"Total score after round {round_number}: {total_score}")

print(f"\nGame Over! Your final score after 5 rounds is: {total_score}")