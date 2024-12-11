from utils import parse_input
from game import SnakeAndLadderGame

def main():
    board_size, snakes, ladders, players = parse_input()
    num_dice = int(input("Enter the number of dice (default is 1): ") or 1)
    game = SnakeAndLadderGame(snakes, ladders, players, board_size, num_dice)
    game.play()

if __name__ == "__main__":
    main()
