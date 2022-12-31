from random import randint

dice_to_roll = int(input("How many dice to roll? \n"))
how_many_sides = int(input("How many sides? \n"))

if dice_to_roll > 0 and how_many_sides > 0:
    while dice_to_roll != "q":
        result = "|"
        for dice in range(dice_to_roll):
            side = randint(1,how_many_sides)
            result += f"{side}|"
        print(result)
        roll_again = input("Roll again? ('q' to quit) \n")


