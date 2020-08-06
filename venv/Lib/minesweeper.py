class Minesweeper:
    def __init__(self, x, y, size, direction):
        self.x = x
        self.y = y
        self.map_x = x * size
        self.map_y = y * size
        self.direction = direction
        self.gCost = 0
        self.hCost = 0

    def FCost(self):
        return self.gCost + self.hCost

    def GetPosition(self):
        return (self.x, self.y, self.direction)

    def TurnRight(self):
        if self.direction == "north":
            self.direction = "east"
        elif self.direction == "east":
            self.direction = "south"
        elif self.direction == "south":
            self.direction = "west"
        elif self.direction == "west":
            self.direction = "north"

    def TurnLeft(self):
        if self.direction == "north":
            self.direction = "west"
        elif self.direction == "west":
            self.direction = "south"
        elif self.direction == "south":
            self.direction = "east"
        elif self.direction == "east":
            self.direction = "north"

    def Move(self, numberOfFields, sizeOfField):
        if self.direction == "north" and self.y != 0:
            self.y = self.y - 1
            self.map_y = self.y * sizeOfField
        elif self.direction == "west" and self.x != 0:
            self.x = self.x - 1
            self.map_x = self.x * sizeOfField
        elif self.direction == "south" and self.y != numberOfFields - 1:
            self.y = self.y + 1
            self.map_y = self.y * sizeOfField
        elif self.direction == "east" and self.x != numberOfFields - 1:
            self.x = self.x + 1
            self.map_x = self.x * sizeOfField
            
    def SetParent(self, parentState, parentAction):
        self.parent = [parentState, parentAction]
            
    def __eq__(self, other):
        return isinstance(other, Minesweeper) and self.x == other.x and self.y == other.y and self.direction == other.direction