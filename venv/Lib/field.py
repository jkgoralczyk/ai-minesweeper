from fieldObject import *

class Field:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.map_x = x * size
        self.map_y = y * size
        self.fieldObject = FieldObject(True)

    def GetPosition(self):
        return (self.x, self.y)