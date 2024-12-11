from collections import deque
from board import Board
from dice import Dice
from player import Player

class SnakeAndLadderGame:
    def __init__(self, snakes, ladders, players, board_size=100, num_dice=1):
        self.board = Board(board_size, snakes, ladders)
        self.players = deque([Player(name) for name in players])
        self.dice = Dice(num_dice=num_dice)
        self.board_size = board_size

    def play(self):
        while len(self.players) > 1:
            player = self.players.popleft()
            dice_value = self.dice.roll()
            initial_position = player.position

            # Consecutive sixes handling
            if dice_value == 6:
                player.consecutive_sixes += 1
            else:
                player.reset_consecutive_sixes()

            if player.consecutive_sixes == 3:
                print(f"{player.name} rolled three consecutive 6s. Cancelling all moves.")
                player.reset_consecutive_sixes()
                self.players.append(player)
                continue

            # Move player
            new_position = initial_position + dice_value
            if new_position > self.board.size:
                new_position = initial_position
            else:
                new_position = self.board.get_new_position(new_position)

            player.position = new_position
            print(f"{player.name} rolled a {dice_value} and moved from {initial_position} to {new_position}")

            # Check for win
            if new_position == self.board.size:
                print(f"{player.name} wins the game!")
                self.players.remove(player)  # Remove player if they win
                if len(self.players) == 1:
                    print(f"{self.players[0].name} is the last player standing and wins the game!")
                    break
            else:
                self.players.append(player)
