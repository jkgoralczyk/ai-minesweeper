import pygame
from minesweeper import Minesweeper
from grid import Grid
from fieldObject import *
from aStar import *
from PIL import Image
import csv
import random
import itertools
import pickle
import numpy as np
import pandas as pd

pygame.init()

display_width = 700
display_height = 700

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('AiMinesweeper')
clock = pygame.time.Clock()

numberOfFields = 10
sizeOfField = display_height / numberOfFields

minesweeperSize = int(sizeOfField * 1)

minesweeperNorthImg = pygame.image.load('images/minesweeperNorth.png')
minesweeperNorthImg = pygame.transform.scale(minesweeperNorthImg, (minesweeperSize, minesweeperSize))

minesweeperSouthImg = pygame.image.load('images/minesweeperSouth.png')
minesweeperSouthImg = pygame.transform.scale(minesweeperSouthImg, (minesweeperSize, minesweeperSize))

minesweeperWestImg = pygame.image.load('images/minesweeperWest.png')
minesweeperWestImg = pygame.transform.scale(minesweeperWestImg, (minesweeperSize, minesweeperSize))

minesweeperEastImg = pygame.image.load('images/minesweeperEast.png')
minesweeperEastImg = pygame.transform.scale(minesweeperEastImg, (minesweeperSize, minesweeperSize))

bombImg = pygame.image.load('images/bomb.png')
bombImg = pygame.transform.scale(bombImg, (minesweeperSize, minesweeperSize))

stoneImg = pygame.image.load('images/stone.png')
stoneImg = pygame.transform.scale(stoneImg, (minesweeperSize, minesweeperSize))

puddleImg = pygame.image.load('images/puddle.png')
puddleImg = pygame.transform.scale(puddleImg, (minesweeperSize, minesweeperSize))

grassImg = pygame.image.load('images/grass.png')

#użycie wyniku działania algorytmu genetycznego do generacji planszy
with open('data/genetics/bombs.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    readerList = list(reader)
    genetics = []
    for i in range(len(readerList[0])):
        if readerList[0][i] == '1':
            genetics.append(i)

mapObject = Grid(numberOfFields, sizeOfField, genetics)
map = mapObject.grid
minesweeper = Minesweeper(0, 0, sizeOfField, "east")
aStar = AStar(mapObject)

[first_field, last_field] = mapObject.FirstAndLast()

def game_loop(startPoint):
    firstloop = True
    currentField = startPoint
    gameExit = False
    fieldsWithBomb = mapObject.fieldsWithBomb
    path = aStar.FindPath(minesweeper, fieldsWithBomb)
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        for y in map:
            for x in y:
                gameDisplay.blit(grassImg, (x.map_x, x.map_y))
                if type(x.fieldObject) is Bomb:
                    gameDisplay.blit(bombImg, (x.map_x, x.map_y))

                if type(x.fieldObject) is Puddle:
                    gameDisplay.blit(puddleImg, (x.map_x, x.map_y))

                if type(x.fieldObject) is Stone:
                    gameDisplay.blit(stoneImg, (x.map_x, x.map_y))

                if x.map_x == minesweeper.map_x and x.map_y == minesweeper.map_y:
                    if minesweeper.direction == "north":
                        gameDisplay.blit(minesweeperNorthImg, (x.map_x, x.map_y))
                    elif minesweeper.direction == "south":
                        gameDisplay.blit(minesweeperSouthImg, (x.map_x, x.map_y))
                    elif minesweeper.direction == "west":
                        gameDisplay.blit(minesweeperWestImg, (x.map_x, x.map_y))
                    elif minesweeper.direction == "east":
                        gameDisplay.blit(minesweeperEastImg, (x.map_x, x.map_y))

        pygame.display.update()

        #użycie sieci neuronowej do rozpoznania trudności planszy
        if firstloop:
            with open('data/neuralNetwork/neuralNetwork3.sav', 'rb') as pickle_file:
                mlp = pickle.load(pickle_file)
            imagePath = 'data/neuralNetwork/map.png'
            pygame.image.save(gameDisplay, imagePath)
            img = Image.open(imagePath).convert('L')
            img = img.resize((150, 150))
            img.save(imagePath)
            img = Image.open(imagePath)
            mapArray = np.array(list(itertools.chain(*np.asarray(img).tolist())))
            mapArray = mapArray.reshape(1, -1)
            prediction = mlp.predict(mapArray)
            firstloop = False
            print('Trudność planszy to: ' + str(prediction[0]))
            print('')

        #użycie drzew decyzyjnych do rozpoznawania bomb
        if [minesweeper.x, minesweeper.y] in fieldsWithBomb:
            #rodzaj
            with open('data/decisionTree/decisionTreeBombType.sav', 'rb') as pickle_file:
                decisionTreeBombType = pickle.load(pickle_file)
            bomb = np.array(map[minesweeper.y][minesweeper.x].fieldObject.getBombParametersForBombType())
            bomb = bomb.reshape(1, -1)
            prediction = decisionTreeBombType.predict(bomb)
            print('Bomba na polu: [' + str(minesweeper.x) + '][' + str(minesweeper.y) + '] to: ' + str(prediction[0]))
            print('Prawdziwa wartość: ' + str(map[minesweeper.y][minesweeper.x].fieldObject.getBombParametersAll()[8]))

            #wybuch
            with open('data/decisionTree/decisionTreeExplode.sav', 'rb') as pickle_file:
                decisionTreeExplode = pickle.load(pickle_file)
            bomb = np.array(map[minesweeper.y][minesweeper.x].fieldObject.getBombParametersForExplode())
            bomb = bomb.reshape(1, -1)
            prediction = decisionTreeExplode.predict(bomb)
            if prediction[0] == 0:
                print('Bomba na polu: [' + str(minesweeper.x) + '][' + str(minesweeper.y) + '] nie wybucha.')
            else:
                print('Bomba na polu: [' + str(minesweeper.x) + '][' + str(minesweeper.y) + '] wybucha.')
            print('Prawdziwa wartość: ' + map[minesweeper.y][minesweeper.x].fieldObject.getBombParametersAll()[7])
            print('')

        if len(path) > 0:
            if path[0] == 'TurnLeft':
                minesweeper.TurnLeft()
            elif path[0] == 'TurnRight':
                minesweeper.TurnRight()
            elif path[0] == 'Move':
                minesweeper.Move(numberOfFields, sizeOfField)
            #print(path[0])
            path.remove(path[0])
        elif len(fieldsWithBomb) > 0:
            fieldsWithBomb.remove(fieldsWithBomb[fieldsWithBomb.index([minesweeper.x, minesweeper.y])])
            if len(fieldsWithBomb) > 0:
                path = aStar.FindPath(minesweeper, fieldsWithBomb)

        clock.tick(4)

game_loop(first_field)
pygame.quit()
quit()