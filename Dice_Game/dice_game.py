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
            game_over = self.check_game_over()
            if game_over:
                break

    def play_round(self):
        # Welcome the user
        self.print_round_welcome()
        # Roll the dice
        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()

        # Show the values
        self.show_dice(player_value, computer_value)

        # Determine winner loser
        if player_value > computer_value:
            self.update_counters(winner=self._player, loser=self._computer)
            print(f"You won the round! 🏆")
        elif computer_value > player_value:
            self.update_counters(winner=self._computer, loser=self._player)
            print(f"The computer won this round! Try again. 😢")
        else:
            print(f"It's a tie! 😎")
        # Show counters
        self.show_counters()


    def print_round_welcome(self):
        print(f"---------New Round---------")
        input("🎲 Press ENTER to roll the dice.🎲")

    def show_dice(self, player_value, computer_value):
        print(f"Your die: {player_value}")
        print(f"Computer die: {computer_value}")

    def update_counters(self, winner, loser):
        winner.decrement_counter()
        loser.increment_counter()

    def show_counters(self):
        print(f"Your counter: {self._player.counter}")
        print(f"Computer counter: {self._computer.counter}")

    def check_game_over(self):
        if self._player.counter == 0:
            self.show_game_over(self._player)
            return True
        elif self._computer.counter == 0:
            self.show_game_over(self._computer)
            return True
        else:
            return False

    def show_game_over(self, winner):
        if winner.is_computer:
            print("\n===========================")
            print("   G A M E       O V E R")
            print("The computer won the game!")
            print("============================= ")
        else:
            print("\n===========================")
            print("   G A M E       O V E R")
            print("You won the game!")
            print("============================= ")
