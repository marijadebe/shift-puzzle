from static.Box import Box
from js import console
from random import randint

class Board:
    def __init__(self, boardSize: int = 4):
        self._boardSize = boardSize
        self._gameState = [[Box(1+i+j*boardSize) for j in range(boardSize)] for i in range(boardSize)]
        self._gameState[boardSize-1][boardSize-1].value = 0

    def drawSelf(self, canvas):
        width = canvas.width
        height = canvas.height
        ctx = canvas.getContext("2d")
        boxSize = width//self._boardSize
        ctx.clearRect(0,0,width,height)

        for x in range(self._boardSize):
            for y in range(self._boardSize):
                self._gameState[x][y].drawSelf(x,y,boxSize,ctx)

    def clickHandler(self, positionX: int, positionY: int, canvas) -> bool:
        width = canvas.width
        height = canvas.height
        boxSize = height//self._boardSize

        x = int(positionX//boxSize)
        y = int(positionY//boxSize)

        if self._gameState[x][y].value != 0:
            if x-1 >= 0 and self._gameState[x-1][y].value == 0:
                self._gameState[x][y].value, self._gameState[x-1][y].value = self._gameState[x-1][y].value, self._gameState[x][y].value
                return True
            elif y-1 >= 0 and self._gameState[x][y-1].value == 0:
                self._gameState[x][y].value, self._gameState[x][y-1].value = self._gameState[x][y-1].value, self._gameState[x][y].value
                return True
            elif x+1 < self._boardSize and self._gameState[x+1][y].value == 0:
                self._gameState[x][y].value, self._gameState[x+1][y].value = self._gameState[x+1][y].value, self._gameState[x][y].value
                return True
            elif y+1 < self._boardSize and self._gameState[x][y+1].value == 0:
                self._gameState[x][y].value, self._gameState[x][y+1].value = self._gameState[x][y+1].value, self._gameState[x][y].value
                return True
        return False

    def shuffleSelf(self):
        #Fischer-Yates algorithm implementation
        arr = list(range(0,self._boardSize**2))
        for i in range(len(arr)-1,0,-1):
            j = randint(0,i)
            arr[i],arr[j] = arr[j],arr[i]
        my_count = 0
        for i, num in enumerate(arr, start=1):
            my_count += sum(num>num2 for num2 in arr[i:]) 
        if not my_count % 2: #if permutation is odd
            arr[0], arr[1] = arr[1], arr[0]
        
        for x in range(self._boardSize):
            for y in range(self._boardSize):
                self._gameState[x][y].value = arr[x*self._boardSize+y]

