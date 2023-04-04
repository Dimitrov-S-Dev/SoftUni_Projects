class DiceGame:

    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def play(self):
        print(f"===========================")
        print(f"🎲 Welcome to Roll the Dice!")
        print(f"============================")
        while True:
            self.play_round()
            # TODO: implement Game Over

    def play_round(self):
        # Welcome the user
        print(f"---------New Round---------")
        input("🎲 Press any key to roll the dice.🎲")
        # Roll the dice
        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()

        # Show the values
        print(f"Your die: {player_value}")
        print(f"Computer die: {computer_value}")

        # Determine winner loser
        if player_value > computer_value:
            self._player.decrement_counter() # Winner
            self._computer.increment_counter() # Loser
            print(f"You won the round!")
        elif computer_value > player_value:
            self._player.increment_counter() # Loser
            self._computer.decrement_counter() # Winner
            print(f"The computer won this round! Try again.")
        else:
            print(f"It's a tie!")
        # Show counters
        print(f"Your counter: {self._player.counter}")
        print(f"Computer counter: {self._computer.counter}")
