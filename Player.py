class Player:

    def     __init__(self, pos_x, pos_y):
        self.player_x = pos_x
        self.player_y = pos_y

    def getX(self):
        return self.player_x

    def getY(self):
        return self.player_y

    def setX(self, new_x: int):
        self.player_x = new_x

    def setY(self, new_y: int):
        self.player_y = new_y

    def getPosition(self):
        return self.player_x, self.player_y

    def setPosition(self, pos: tuple):
        self.player_x = pos[0]
        self.player_y = pos[1]

    def moveRelative(self, move: tuple) -> tuple:
        self.player_x += move[0]
        self.player_y += move[1]

        return self.player_x, self.player_y
