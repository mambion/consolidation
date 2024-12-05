import random

# Define global dice variables
dice1 = 0
dice2 = 0
dice3 = 0

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



def check_matches():
    global dice1, dice2, dice3
    if dice1 == dice2 == dice3:
        print("You have tupled out!")
    else:
        if dice1 == dice2:
            print("Dice 1 and Dice 2 are locked.")
        if dice1 == dice3:
            print("Dice 1 and Dice 3 are locked.")
        if dice2 == dice3:
            print("Dice 2 and Dice 3 are locked.")
        total = [dice1, dice2, dice3]
        print("Your current total is", sum(total), "| Dice 1:", dice1, "Dice 2:", dice2, "Dice 3:", dice3)

def unlocked_reroll():
    global dice1, dice2, dice3
    re_roll = None
    choice = input("Would you like to re-roll one of the dice? (y/n) ")
    if choice.lower() == "y" and dice1 != dice2 and dice1 != dice3 and dice2 != dice3:
        re_roll = input("Which dice do you want to re-roll? (1, 2, or 3) ")
    elif re_roll == "1":
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

# dice1 = 1
# dice2 = 6
# dice3 = 6

def locked_reroll():
    global dice1, dice2, dice3
    locked_choice = input("Would you like to re-roll the unlocked dice? (y/n) ")
    if locked_choice.lower() == "y":
        if dice1 != dice2 and dice1 != dice3 and dice2 == dice3:
            print("You can only re-roll Dice 1.")
            input("Press 'enter' to re-roll dice 1.")
            dice1 = random.choice([1, 2, 3, 4, 5, 6])
            print("New dice 1:", dice1)
        elif dice1 != dice2 and dice1 == dice3 and dice2 != dice3:
            print("You can only re-roll Dice 2.")
            input("Press 'enter' to re-roll dice 2.")
            dice2 = random.choice([1, 2, 3, 4, 5, 6])
            print("New dice 2:", dice2)
        elif dice1 == dice2 and dice1 != dice3 and dice2 != dice3:
            print("You can only re-roll Dice 3.")
            input("Press 'enter' to re-roll dice 3.")
            dice3 = random.choice([1, 2, 3, 4, 5, 6])
            print("New dice 3:", dice3)
    
    else:
        print("You have chosen to stand with your current total.")

# Start the game
print("Welcome to Tuple Out! Click 'enter' to see the rules of the game:")
# ... (rules here)
print("1. You have 3 dice and you will roll each dice once.")
input()
print("2. When you've rolled each dice, you will have the chance to re-roll your lowest number.")
input()
print("3. However, if you've you roll the same number, those dice will lock.")
input()
print("4. And if you roll the same number three times in a row, you will not get nay points for the round.")
input()
print("5. Write down your totals after each round! And whoever has the most points after 5 rounds wins!")
input()

# random_roll()
# check_matches()

def totals():
    if dice1 == dice2 == dice3:
        print("You lost this round!")
    else:
        total = [dice1, dice2, dice3]
        print("Your total for the round is", sum(total), "| Dice 1:", dice1, "Dice 2:", dice2, "Dice 3:", dice3)
# Ask to re-roll with locked dice
if dice1 != dice2 and dice1 != dice3 and dice2 == dice3:
    locked_reroll()
elif dice1 != dice2 and dice1 == dice3 and dice2 != dice3:
    locked_reroll()
elif dice1 == dice2 and dice1 != dice3 and dice2 != dice3:
    locked_reroll()

# Ask to re-roll
if dice1 != dice2 and dice1 != dice3 and dice2 != dice3:
    unlocked_reroll()


# Print totals
# totals()

def play_game():
    total_score = 0
    for round_number in range(1, 6):
        print(f"\n--- Round {round_number} ---")
        random_roll()
        check_matches()
        if dice1 != dice2 and dice1 != dice3 and dice2 == dice3:
            locked_reroll()
        elif dice1 != dice2 and dice1 == dice3 and dice2 != dice3:
            locked_reroll()
        elif dice1 == dice2 and dice1 != dice3 and dice2 != dice3:
            locked_reroll()
        if dice1 != dice2 and dice1 != dice3 and dice2 != dice3:
            unlocked_reroll()
        total_score += sum([dice1, dice2, dice3])
        print(f"Total score after round {round_number}: {total_score}")

    print(f"\nGame Over! Your final score after 5 rounds is: {total_score}")
play_game()
