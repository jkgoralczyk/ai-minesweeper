import random

class FieldObject:
    def __init__(self, isWalkable):
        self.isWalkable = isWalkable
        
class Stone(FieldObject):
    def __init__(self):
        FieldObject.__init__(self, False)

class Puddle(FieldObject):
    def __init__(self):
        FieldObject.__init__(self, True)

class Bomb(FieldObject):
    def __init__(self, bombType):
        FieldObject.__init__(self, True)
        self.generateBomb(bombType)

    def generateBomb(self, bombType):
        led = ['yes', 'no']
        timer = ['yes', 'no']
        keyboard = ['yes', 'no']
        shape = ['rectangle', 'oval', 'square']
        color = ['black', 'grey']
        self.bombType = bombType
        if self.bombType == 0:
            self.weight = random.randrange(1, 40, 1)
            self.power = random.randrange(100, 300, 1)
            self.led = random.choice(led)
            self.timer = 'yes'
            self.keyboard = 'no'
            self.shape = random.choice(shape)
            self.color = 'black'
            self.defuseTime = 10
            if (self.led == 'yes' and self.power > 200) or self.shape == 'oval':
                self.explode = 'yes'
            else:
                self.explode = 'no'
        if self.bombType == 1:
            self.weight = random.randrange(1, 30, 1)
            self.power = random.randrange(300, 500, 1)
            self.led = 'yes'
            self.timer = random.choice(timer)
            self.keyboard = 'yes'
            self.shape = 'rectangle'
            self.color = random.choice(color)
            self.defuseTime = 20
            if (self.timer == 'yes' and self.power > 400) or self.color == 'black':
                self.explode = 'yes'
            else:
                self.explode = 'no'
        if self.bombType == 2:
            self.weight = random.randrange(30, 60, 1)
            self.power = random.randrange(150, 250, 1)
            self.led = 'no'
            self.timer = random.choice(timer)
            self.keyboard = 'no'
            self.shape = random.choice(shape)
            self.color = 'grey'
            self.defuseTime = 45
            if (self.led == 'yes' or self.timer == 'yes') and self.power > 200:
                self.explode = 'yes'
            else:
                self.explode = 'no'
        if self.bombType == 3:
            self.weight = random.randrange(30, 50, 1)
            self.power = random.randrange(350, 500, 1)
            self.led = random.choice(led)
            self.timer = random.choice(timer)
            self.keyboard = random.choice(keyboard)
            self.shape = random.choice(shape)
            self.color = 'black'
            self.defuseTime = 89
            if (self.timer == 'yes' and self.weight > 40) or self.keyboard == 'yes':
                self.explode = 'yes'
            else:
                self.explode = 'no'
        if self.bombType == 4:
            self.weight = random.randrange(50, 80, 1)
            self.power = random.randrange(400, 500, 1)
            self.led = random.choice(led)
            self.timer = random.choice(timer)
            self.keyboard = 'yes'
            self.shape = 'square'
            self.color = random.choice(color)
            self.defuseTime = 67
            if (self.led == 'yes' or self.timer == 'yes') and self.weight > 55:
                self.explode = 'yes'
            else:
                self.explode = 'no'
        if self.bombType == 5:
            self.weight = random.randrange(60, 100, 1)
            self.power = random.randrange(200, 400, 1)
            self.led = 'yes'
            self.timer = 'no'
            self.keyboard = random.choice(keyboard)
            self.shape = 'rectangle'
            self.color = random.choice(color)
            self.defuseTime = 40
            if (self.led == 'yes' and self.weight > 60) or self.keyboard == 'yes':
                self.explode = 'yes'
            else:
                self.explode = 'no'
        if self.bombType == 6:
            self.weight = random.randrange(60, 100, 1)
            self.power = random.randrange(100, 150, 1)
            self.led = 'no'
            self.timer = random.choice(timer)
            self.keyboard = 'yes'
            self.shape = 'oval'
            self.color = 'grey'
            self.defuseTime = 28
            if (self.led == 'yes' or self.timer == 'yes') and (self.weight > 80 or self.power > 300):
                self.explode = 'yes'
            else:
                self.explode = 'no'
        if self.bombType == 7:
            self.weight = random.randrange(10, 100, 1)
            self.power = random.randrange(100, 150, 1)
            self.led = random.choice(led)
            self.timer = random.choice(timer)
            self.keyboard = 'no'
            self.shape = 'square'
            if self.weight < 50:
                self.color = 'grey'
            else:
                self.color = random.choice(color)
            self.defuseTime = 45
            if (self.timer == 'yes' and self.weight > 80) or self.color == 'grey':
                self.explode = 'yes'
            else:
                self.explode = 'no'

    def getBombParametersForBombType(self):
        parameters = self.changeParametersToNumerical()
        return [parameters[0], parameters[1], parameters[2], parameters[3], parameters[4], parameters[5], parameters[6]]

    def getBombParametersForExplode(self):
        parameters = self.changeParametersToNumerical()
        return [parameters[0], parameters[1], parameters[2], parameters[3], parameters[4], parameters[5], parameters[6], parameters[8]]

    def getBombParametersAll(self):
        return [self.weight, self.power, self.led, self.timer, self.keyboard, self.shape, self.color, self.explode, self.bombType]

    def changeParametersToNumerical(self):
        if self.led == 'no':
            led = 0
        else:
            led = 1
        if self.timer == 'no':
            timer = 0
        else:
            timer = 1
        if self.keyboard == 'no':
            keyboard = 0
        else:
            keyboard = 1
        if self.shape == 'rectangle':
            shape = 0
        elif self.shape == 'oval':
            shape = 1
        else:
            shape = 2
        if self.color == 'black':
            color = 0
        else:
            color = 1
        if self.explode == 'no':
            explode = 0
        else:
            explode = 1
        return [self.weight, self.power, led, timer, keyboard, shape, color, explode, self.bombType]
