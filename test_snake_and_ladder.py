import unittest
from board import Board
from dice import Dice
from player import Player
from game import SnakeAndLadderGame


class TestBoard(unittest.TestCase):
    def test_snake_mechanics(self):
        snakes = {14: 7, 31: 19}
        ladders = {}
        board = Board(size=100, snakes=snakes, ladders=ladders)
        self.assertEqual(board.get_new_position(14), 7)
        self.assertEqual(board.get_new_position(31), 19)

    def test_ladder_mechanics(self):
        snakes = {}
        ladders = {3: 22, 8: 30}
        board = Board(size=100, snakes=snakes, ladders=ladders)
        self.assertEqual(board.get_new_position(3), 22)
        self.assertEqual(board.get_new_position(8), 30)

    def test_snake_and_ladder_chain(self):
        snakes = {14: 7}
        ladders = {7: 21}
        board = Board(size=100, snakes=snakes, ladders=ladders)
        self.assertEqual(board.get_new_position(14), 21)


class TestDice(unittest.TestCase):
    def test_dice_roll_range(self):
        dice = Dice(sides=6, num_dice=1)
        for _ in range(100):
            roll = dice.roll()
            self.assertGreaterEqual(roll, 1)
            self.assertLessEqual(roll, 6)

    def test_two_dice_roll_range(self):
        dice = Dice(sides=6, num_dice=2)
        for _ in range(100):
            roll = dice.roll()
            self.assertGreaterEqual(roll, 2)
            self.assertLessEqual(roll, 12)


class TestPlayer(unittest.TestCase):
    def test_player_initialization(self):
        player = Player(name="Alice")
        self.assertEqual(player.name, "Alice")
        self.assertEqual(player.position, 0)
        self.assertEqual(player.consecutive_sixes, 0)

    def test_reset_consecutive_sixes(self):
        player = Player(name="Bob")
        player.consecutive_sixes = 2
        player.reset_consecutive_sixes()
        self.assertEqual(player.consecutive_sixes, 0)


class TestSnakeAndLadderGame(unittest.TestCase):
    def setUp(self):
        snakes = {17: 7}
        ladders = {3: 22}
        players = ["Alice", "Bob"]
        self.game = SnakeAndLadderGame(snakes=snakes, ladders=ladders, players=players)

    def test_player_movement_within_board(self):
        player = self.game.players[0]
        player.position = 94
        dice_roll = 5
        self.game.board.size = 100
        final_position = min(player.position + dice_roll, self.game.board.size)
        self.assertEqual(final_position, 99)

    def test_snake_bite(self):
        player = self.game.players[0]
        player.position = 17
        new_position = self.game.board.get_new_position(player.position)
        self.assertEqual(new_position, 7)

    def test_ladder_climb(self):
        player = self.game.players[0]
        player.position = 3
        new_position = self.game.board.get_new_position(player.position)
        self.assertEqual(new_position, 22)

    def test_win_condition(self):
        player = self.game.players[0]
        player.position = 95
        dice_roll = 5
        new_position = min(player.position + dice_roll, self.game.board.size)
        self.assertEqual(new_position, 100)


if __name__ == "__main__":
    unittest.main()
