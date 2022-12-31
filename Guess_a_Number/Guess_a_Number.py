import random

computer_number = random.randint(1, 100)

while True:
    player_input = input("Guess the number between (1 -> 100):\n")
    if player_input.isdigit():
        player_number = int(player_input)
        if player_number == computer_number:
            print("You guess it!")
            break
        elif player_number > computer_number:
            print("Too High!")
        else:
            print("Too Low!")


