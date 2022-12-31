from random import randint
rock = "Rock"
paper = "Paper"
scissors = "Scissors"
player_move = input("Choose [r]-> rock, [p]->paper or [s]->scissors:\n")

if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid Input. Try again...")

comp_random_number = randint(1, 3)
comp_move = ""

if comp_random_number == 3:
    comp_move = rock
elif comp_random_number == 2:
    comp_move = scissors
elif comp_random_number == 1:
    comp_move = paper
print(f"Computer move => {comp_move}")

if (player_move == rock and comp_move == scissors) or \
        (player_move == paper and comp_move == rock) or \
        (player_move == scissors and comp_move == paper):
    print("You win!")
elif player_move == comp_move:
    print("Draw!")
else:
    print("You Lose!")