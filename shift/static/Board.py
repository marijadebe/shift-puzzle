from static.Box import Box
from js import console
class Board:
    def __init__(self, boardSize: int = 4):
        self._boardSize = boardSize
        self._gameState = [[Box(1+i+j*boardSize) for j in range(boardSize)] for i in range(boardSize)]
        self._gameState[boardSize-1][boardSize-1].value = 0

    def drawSelf(self, canvas):
        width = canvas.getBoundingClientRect().width
        height = canvas.getBoundingClientRect().height
        ctx = canvas.getContext("2d")
        boxSize = width//self._boardSize

        for x in range(self._boardSize):
            for y in range(self._boardSize):
                self._gameState[x][y].drawSelf(x,y,boxSize,ctx)

    def shuffleSelf(self):
        pass