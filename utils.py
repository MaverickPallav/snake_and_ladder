import random

def parse_input():
    board_size = int(input("Enter board size (default is 100): ") or 100)
    num_snakes = int(input("Enter the number of snakes: "))
    num_ladders = int(input("Enter the number of ladders: "))
    num_players = int(input("Enter the number of players: "))
    
    print("Enter the names of the players:")
    players = [input().strip() for _ in range(num_players)]

    # Generate snakes and ladders
    snakes, ladders = generate_snakes_and_ladders(board_size, num_snakes, num_ladders)

    return board_size, snakes, ladders, players

def generate_snakes_and_ladders(board_size, num_snakes, num_ladders):
    snakes = {}
    ladders = {}
    positions = set()

    # Generate snakes
    for _ in range(num_snakes):
        while True:
            head = random.randint(2, board_size - 1)
            tail = random.randint(1, head - 1)
            if head not in positions and tail not in positions:
                snakes[head] = tail
                positions.add(head)
                positions.add(tail)
                break

    # Generate ladders
    for _ in range(num_ladders):
        while True:
            start = random.randint(1, board_size - 2)
            end = random.randint(start + 1, board_size - 1)
            if start not in positions and end not in positions:
                ladders[start] = end
                positions.add(start)
                positions.add(end)
                break

    return snakes, ladders
