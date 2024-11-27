# Tuple out 5.0!
print("Welcome to Tuple Out! Here are the rules of the game:")
print("1. You have 3 dice and you will roll each dice once.")
print("2. When you've rolled each dice, you will have the chance to re-roll your lowest number.")
print("3. However, if you've you roll the same number, those dice will lock.")
print("4. And if you roll the same number three times in a row, you will not get nay points for the round.")
print("5. Write down your totals after each round! And whoever has the most points after 5 rounds wins!")
import random

# Roll each dice to get a single integer

input("Hit any key to roll dice 1.") 
dice1 = random.choice([1, 2, 3, 4, 5, 6])
print("Dice 1:", dice1)
input("Hit any key to roll dice 2.")
dice2 = random.choice([1, 2, 3, 4, 5, 6])
print("Dice 2:", dice2)
input("Hit any key to roll dice 3.")
dice3 = random.choice([1, 2, 3, 4, 5, 6])
print("Dice 3:", dice3)

# Check for matches
if dice1 == dice2 == dice3:
    print("You have Tripled Out!")
else:
    if dice1 == dice2:
        print("Dice 1 and Dice 2 are locked.")
    if dice1 == dice3:
        print("Dice 1 and Dice 3 are locked.")
    if dice2 == dice3:
        print("Dice 2 and Dice 3 are locked.")
total = [dice1, dice2, dice3]

# Ask the if they want to re-roll without locked dice
if dice1 != dice2 and dice1 != dice3 and dice2 != dice3:
    print("Your current total is", sum(total), "| Dice 1:", dice1, "Dice 2:", dice2, "Dice 3:", dice3,)
    re_roll = input("Which dice do you want to re-roll? (1, 2, or 3) ")
    if re_roll == "1":
        input("Press any key to re-roll dice 1.")
        dice1 = random.choice([1, 2, 3, 4, 5])
        print("New dice 1: ", dice1)
    if re_roll == "2":
        input("Press any key to re-roll dice 2.")
        dice2 = random.choice([1, 2, 3, 4, 5])
        print("New dice 2: ", dice2)
    if re_roll == "3":
        input("Press any key to re-roll dice 3.")
        dice3 = random.choice([1, 2, 3, 4, 5])
        print("New dice 3: ", dice3)

# Sum the dice values
total = [dice1, dice2, dice3]
print("Your current total is", sum(total), "| Dice 1:", dice1, "Dice 2:", dice2, "Dice 3:", dice3,)

# Ask if the user wants to re-roll with locked dice
if dice1 == dice2 == dice3:
    input("Hit any key to continue to the next round.")
else: 
    input("Hit any key to continue.")
if dice1 == dice2 != dice3:
    print("You can only re-roll dice 3.")
    input("Hit any key to roll dice 3.")
    dice1 = random.choice([1, 2, 3, 4, 5, 6])
    print("New Dice 1:", dice1)
elif dice1 == dice3 != dice2:
    print("You can only re-roll dice 2.")
    input("Hit any key to roll dice 2.")
    dice1 = random.choice([1, 2, 3, 4, 5, 6])
    print("New Dice 1:", dice1)
elif dice2 == dice3 != dice1:
    print("You can only re-roll dice 1.")
    input("Hit any key to roll dice 1.")
    dice1 = random.choice([1, 2, 3, 4, 5, 6])
    print("New Dice 1:", dice1)

    # Add new totals
    total = [dice1, dice2, dice3]
    print("Your new total is", sum(total))

# Print the final score
print("Total sum of dice:", sum(total))

# Ask to play another round
input("Would you like to play another round? Run the program again to play again.")