from field import Field
from fieldObject import *
from minesweeper import Minesweeper
import random


class Grid:

    def __init__(self, numberOfFields, sizeOfField, genetics):
        self.grid = []
        self.numberOfFields = numberOfFields
        self.sizeOfField = sizeOfField
        self.drawingSize = numberOfFields * sizeOfField
        self.fieldsWithBomb = self.GenerateFieldsWithBomb()

        for y in range(0, numberOfFields):
            horizontal = []
            for x in range(0, numberOfFields):
                field = Field(x, y, sizeOfField)
                if self.IsBomb(field.x, field.y):
                    field.fieldObject = Bomb(random.choice(genetics))
                elif self.IsPuddle(field.x, field.y):
                    field.fieldObject = Puddle()
                elif self.IsStone(field.x, field.y):
                    field.fieldObject = Stone()
                horizontal.insert(len(horizontal), field)
            self.grid.insert(len(self.grid), horizontal)

    def IsBomb(self, x, y):
        if [x, y] in self.fieldsWithBomb:
            return True

    def IsPuddle(self, x, y):
        if x == 0 and y == 0:
            return False
        else:
            return random.randrange(10) == 1

    def IsStone(self, x, y):
        if x == 0 and y == 0:
            return False
        else:
            return random.randrange(7) == 1

    def GenerateFieldsWithBomb(self):
        fieldsWithBomb = []
        bombAmount = random.randrange(5, 16, 5)
        while len(fieldsWithBomb) < bombAmount:
            x = random.randrange(10)
            y = random.randrange(10)
            if x != 0 or y != 0:
                if [x, y] not in fieldsWithBomb:
                    fieldsWithBomb.insert(0, [x, y])
        return fieldsWithBomb
                
    def FirstAndLast(self):
            last = self.numberOfFields - 1
            return [self.grid[0][0], self.grid[last][last]]