from random import randint
"""
Create a script that rolls dice for a user.  
When the script runs, it should ask a user how many dice they want to roll 
and how many sides each die will have.
Then it randomly rolls those dice and prints the result.
Every time a user hits Enter, the dice are rolled again.
If a user every enter “q”, then the script quits and stops running!

"""
dice_to_roll = int(input("How many dice to roll? \n"))
how_many_sides = int(input("How many sides? \n"))

if dice_to_roll > 0 and how_many_sides > 0:
    while dice_to_roll != "q":
        result = "|"
        for dice in range(dice_to_roll):
            side = randint(1,how_many_sides)
            result += f"{side}|"
        print(f"Output is:\n{result}")
        roll_again = input("Roll again? ('q' to quit) \n")


