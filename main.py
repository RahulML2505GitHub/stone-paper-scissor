import random
import os
import sys


class Game:

    variables = "stone", "paper", "sissor"

    def __init__(self, player_1: str, player_2: str = "Computer"):
        self.get_clean()
        self.name = f"{self.a}, {self.b} & {self.c} Game".capitalize()
        self.players: tuple[str, str] = player_1.capitalize(), player_2.capitalize()

        print("Wellcome The simple", self.name + "\n")

    def get_clean(self):
        if sys.platform == "win32":
            os.system("cls")

        elif sys.platform == "linux":
            os.system("clear")

    @property
    def a(self):
        return self.variables[0]

    @property
    def b(self):
        return self.variables[1]

    @property
    def c(self):
        return self.variables[2]

    def game_win(self, player_1, player_2):
        if player_1 == player_2:
            return -1

        elif player_1 == self.a:
            if player_2 == self.b:
                return 1
            else:
                return 0

        elif player_1 == self.b:
            if player_2 == self.c:
                return 1
            else:
                return 0

        elif player_1 == self.c:
            if player_2 == self.a:
                return 1
            else:
                return 0

    def play(self):
        pass

    def run(self):
        running = True
        while running:
            print(f"Take a choice from bellow:\n1. {self.a.capitalize()}\n2. {self.b.capitalize()}\n3. {self.c.capitalize()}\n")
            user_choice = input("⏩ ")

            user_choice = int(user_choice) - 1
            comp = self.variables[random.randint(0, 2)]

            winner = self.game_win(self.variables[user_choice], comp)

            if winner>-1:
                print(f"The Winner is {self.players[winner]}!")
            else:
                print("The Game Tied!")
            print()


if __name__ == "__main__":
    app = Game("Rahul")
    app.run()
