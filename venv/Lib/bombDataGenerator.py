import numpy as np
import random
from fieldObject import *

data = np.asarray([['weight', 'power', 'led', 'timer', 'keyboard', 'shape', 'color', 'explode', 'bombType']])

for i in range(500):
    bomb = Bomb(random.randrange(8))
    bombData = bomb.changeParametersToNumerical()
    data = np.vstack([data, bombData])

np.savetxt("data/decisionTree/data.csv", data, delimiter=",", fmt='%s')