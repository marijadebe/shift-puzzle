from js import console
from random import randint
from itertools import chain

class Board:
    def __init__(self, boardSize: int = 4):
        self._boardSize = boardSize
        self._gameState = [[Box(1+i+j*boardSize) for j in range(boardSize)] for i in range(boardSize)]

    def drawSelf(self, canvas):
        """ Procedura pro vykresleni hraci plochy.

        Args:
            canvas (Object): DOM reprezentace hraci plochy.
        """
        width = canvas.width
        height = canvas.height
        ctx = canvas.getContext("2d")
        boxSize = width//self._boardSize
        ctx.clearRect(0,0,width,height)

        for x in range(self._boardSize):
            for y in range(self._boardSize):
                if self._gameState[x][y].value == self._boardSize**2: self._gameState[x][y].drawSelf(x,y,boxSize,ctx, True)
                else: self._gameState[x][y].drawSelf(x,y,boxSize,ctx)

    def keyHandler(self, posX: int, posY: int, canvas) -> bool:
        """Procedura pro ovladani klavesnici

        Args:
            posX (int): Relativni posun po ose X (nabyva hodnot -1,0,1).
            posY (int): Relativni posun po ose Y (nabyva hodnot -1,0,1).
            canvas (Object): DOM reprezentace hraci plochy.

        Returns:
            bool: Uspesnost provedeni tahu, tzn. jeho legalita.
        """
        for x in range(self._boardSize):
            for y in range(self._boardSize):
                if self._gameState[x][y].value == self._boardSize**2:
                    if 0 <= x+posX < self._boardSize and 0 <= y+posY < self._boardSize:
                        self._gameState[x][y].value = self._gameState[x+posX][y+posY].value
                        self._gameState[x+posX][y+posY].value = self._boardSize**2
                        return True
        return False
    def clickHandler(self, positionX: int, positionY: int, canvas) -> bool:
        """Procedura pro ovladani mysi

        Args:
            positionX (int): Posice na ose X kliknuti relativne k vykreslovacimu platnu.
            positionY (int): Posice na ose X kliknuti relativne k vykreslovacimu platnu.
            canvas (Object): DOM reprezentace hraci plochy.

        Returns:
            bool: Uspesnost provedeni tahu, tzn. jeho legalita.
        """
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

    def getPermutationSign(self) -> bool:
        """Spocita znamenko permutace daneho poctem cyklu sude delky.

        Returns:
            bool: Hodnota True znamena, ze je permutace suda.
        """
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
        """Zamichej hraci plochu tak, ze dana permutace je suda a volne misto zustane v pravem dolnim rohu."""
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
        """Dosahli jsme stavu vyhry?

        Returns:
            bool
        """
        for x in range(self._boardSize):
            for y in range(self._boardSize):
                if (x*self._boardSize+y+1 != self._gameState[y][x].value): return False
        return True