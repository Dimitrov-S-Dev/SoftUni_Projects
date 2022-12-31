toothpicks = 13
"""
Implement a version of the “classic” matchsticks/toothpicks two player game.
We start with 13 toothpicks, and plays take turns removing 1, 2, or 3 toothpicks at a time.
The person who removes the last toothpick wins.

"""
print("Welcome To The Game!")
print("*******************")
first_player = input("Enter player 1's name:\n")
second_player = input("Enter player 2's name:\n")
current_player = first_player

while True:
    print(f"{'|' * toothpicks}")
    print(f"There are {toothpicks} toothpicks left")
    choice = int(input(f"How many do you take,{current_player}?\n"))
    if choice < 4:
        toothpicks -= choice
    else:
        print("You can only choose 1, 2 or 3!")
    if toothpicks <= 0:
        print(f"{current_player} wins the game!")
        break
    if current_player == first_player:
        current_player = second_player
    else:
        current_player = first_player
print("GAME OVER!!")
