class Board:
    def __init__(self, size=100, snakes=None, ladders=None):
        self.size = size
        self.snakes = snakes or {}
        self.ladders = ladders or {}

    def get_new_position(self, position):
        # Adjust position until no more snakes/ladders are found
        while position in self.snakes or position in self.ladders:
            if position in self.snakes:
                position = self.snakes[position]
            elif position in self.ladders:
                position = self.ladders[position]
        return position
