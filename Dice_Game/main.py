from die import Die
from player import Player
from dice_game import DiceGame

# Dice Instances
player_die = Die()
computer_die = Die()

# Players Instances
my_player = Player(player_die, is_computer=False)
computer_player = Player(computer_die, is_computer=True)

game = DiceGame(my_player, computer_player)

# Start the Game
game.play()
