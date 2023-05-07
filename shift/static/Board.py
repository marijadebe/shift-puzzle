from js import console
from random import randint
from itertools import chain

class Board:
    def __init__(self, boardSize: int = 4):
        self._boardSize = boardSize
        self._gameState = [[Box(1+i+j*boardSize) for j in range(boardSize)] for i in range(boardSize)]

    def drawSelf(self, canvas):
        width = canvas.width
        height = canvas.height
        ctx = canvas.getContext("2d")
        boxSize = width//self._boardSize
        ctx.clearRect(0,0,width,height)

        for x in range(self._boardSize):
            for y in range(self._boardSize):
                if self._gameState[x][y].value == self._boardSize**2: self._gameState[x][y].drawSelf(x,y,boxSize,ctx, True)
                else: self._gameState[x][y].drawSelf(x,y,boxSize,ctx)

    def clickHandler(self, positionX: int, positionY: int, canvas) -> bool:
        width = canvas.width
        height = canvas.height
        boxSize = height//self._boardSize

        x = int(positionX//boxSize)
        y = int(positionY//boxSize)

        if self._gameState[x][y].value != self._boardSize**2:
            if x-1 >= 0 and self._gameState[x-1][y].value == self._boardSize**2:
                self._gameState[x][y].value, self._gameState[x-1][y].value = self._gameState[x-1][y].value, self._gameState[x][y].value
                return True
            elif y-1 >= 0 and self._gameState[x][y-1].value == self._boardSize**2:
                self._gameState[x][y].value, self._gameState[x][y-1].value = self._gameState[x][y-1].value, self._gameState[x][y].value
                return True
            elif x+1 < self._boardSize and self._gameState[x+1][y].value == self._boardSize**2:
                self._gameState[x][y].value, self._gameState[x+1][y].value = self._gameState[x+1][y].value, self._gameState[x][y].value
                return True
            elif y+1 < self._boardSize and self._gameState[x][y+1].value == self._boardSize**2:
                self._gameState[x][y].value, self._gameState[x][y+1].value = self._gameState[x][y+1].value, self._gameState[x][y].value
                return True
        return False
    #True's even
    def getPermutationSign(self) -> bool:
        flat = [[self._gameState[x][y].value-1,False] for y in range(self._boardSize) for x in range(self._boardSize)]
        cycles = []
        posFix = 0
        while posFix < len(flat):
            if flat[posFix][1] != True:
                pos = posFix
                cycleLength = 0
                while flat[pos][1] != True:
                    cycleLength += 1
                    flat[pos][1] = True
                    pos = flat[pos][0]
                if cycleLength > 1: cycles.append(cycleLength)
            posFix += 1
        countEvenCycles = 0
        for i in cycles:
            if i % 2 == 0: countEvenCycles += 1
        if len(cycles) == 0: return True
        elif len(cycles) > 0 and countEvenCycles == 0: return False
        else: return countEvenCycles % 2 == 0

    def shuffleSelf(self):
        while True:
            for _ in range(12):
                while True:
                    posOneX, posOneY = randint(0,self._boardSize-1), randint(0,self._boardSize-1)
                    posTwoX, posTwoY = randint(0,self._boardSize-1), randint(0,self._boardSize-1)
                    if posOneX != posTwoY or posOneY != posTwoY: break
                if (posOneX != self._boardSize-1 or posOneY != self._boardSize-1) and (posTwoX != self._boardSize-1 or posTwoY != self._boardSize-1):
                    swap = self._gameState[posOneX][posOneY].value
                    self._gameState[posOneX][posOneY].value = self._gameState[posTwoX][posTwoY].value
                    self._gameState[posTwoX][posTwoY].value = swap
            if not self.isInWonState() and self.getPermutationSign(): break

    def isInWonState(self) -> bool:
        for x in range(self._boardSize):
            for y in range(self._boardSize):
                if (x*self._boardSize+y+1 != self._gameState[y][x].value): return False
        return True