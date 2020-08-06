import time
import copy
from minesweeper import Minesweeper
from fieldObject import *

class AStar:
    def __init__(self, grid):
        self.grid = grid

    def FindPath(self, initialState, goalState):
        openSet = []
        closedSet = []
        openSet.insert(0, initialState)

        while len(openSet) > 0:
            currentState = openSet[0]
            for openState in openSet:
                if openState.FCost() < currentState.FCost() or openState.FCost() == currentState.FCost() and openState.hCost < currentState.hCost:
                    currentState = openState
            openSet.remove(currentState)
            closedSet.insert(len(closedSet), currentState)

            if self.GoalTest(currentState, goalState):
                return self.RetracePath(currentState)

            for possibleAction in self.Actions(currentState):
                possibleState = self.Result(currentState, possibleAction)
                possibleState.SetParent(currentState, possibleAction)
                possibleState.hCost = self.Heuristic(possibleState, goalState)
                if possibleState not in openSet:
                    openSet.insert(len(openSet), possibleState)

    def Actions(self, state):
        possibleActions = ['Move', 'TurnLeft', 'TurnRight']
        x, y, direction = state.GetPosition()

        if x == 0 and direction == 'west':
            if 'Move' in possibleActions:
                possibleActions.remove('Move')
        if y == 0 and direction == 'north':
            if 'Move' in possibleActions:
                possibleActions.remove('Move')
        if x == self.grid.numberOfFields - 1 and direction == 'east':
            if 'Move' in possibleActions:
                possibleActions.remove('Move')
        if y == self.grid.numberOfFields - 1 and direction == 'south':
            if 'Move' in possibleActions:
                possibleActions.remove('Move')

        return possibleActions

    def Result(self, state, action):
        x, y, direction = state.GetPosition()
        newState = Minesweeper(0, 0, self.grid.sizeOfField, 'north')
        newState = copy.copy(state)

        if action == 'Move':
            newState.Move(self.grid.numberOfFields, self.grid.sizeOfField)
            newState.gCost += self.ActionCost(newState, action)
        elif action == 'TurnLeft':
            newState.TurnLeft()
            newState.gCost += self.ActionCost(newState, action)
        elif action == 'TurnRight':
            newState.TurnRight()
            newState.gCost += self.ActionCost(newState, action)

        return newState

    def GoalTest(self, state, goals):
        for goal in goals:
            if state.GetPosition()[0] == goal[0] and state.GetPosition()[1] == goal[1]:
                return True
        return False

    def Heuristic(self, state, goals):
        x1, y1 = state.GetPosition()[0], state.GetPosition()[1]
        x2, y2 = goals[0]
        manhattan = abs(x2 - x1) + abs(y2 - y1)
        for goal in goals:
            x2, y2 = goal
            if abs(x2 - x1) + abs(y2 - y1) < manhattan:
                manhattan = abs(x2 - x1) + abs(y2 - y1)
        return manhattan

    def ActionCost(self, state, action):
        if action == 'TurnLeft' or action == 'TurnRight':
            return 1
        elif type(self.grid.grid[state.y][state.x].fieldObject) is Bomb:
            return 1
        elif type(self.grid.grid[state.y][state.x].fieldObject) is Puddle:
            return 5
        elif type(self.grid.grid[state.y][state.x].fieldObject) is Stone:
            return 250000
        else:
            return 1

    def RetracePath(self, state):
        path = []
        while hasattr(state, 'parent'):
            if hasattr(state, 'parent'):
                path.insert(0, state.parent[1])
            state = state.parent[0]
        return path