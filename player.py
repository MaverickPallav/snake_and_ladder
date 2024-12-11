class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.consecutive_sixes = 0

    def reset_consecutive_sixes(self):
        self.consecutive_sixes = 0
