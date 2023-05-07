class Box:
    def __init__(self, value: int = 0):
        if value < 0:
            raise ValueError("Box value has to be a nonnegative integer.")
        else:
            self._value = value 

    def drawSelf(self, x: int, y: int, boxSize: int, ctx, isLast: bool = False):
        ctx.beginPath()
        ctx.fillStyle = "#083b8c"
        ctx.fillRect(boxSize*x, boxSize*y, boxSize, boxSize)
        ctx.closePath()
        if not isLast:
            ctx.beginPath()
            ctx.fillStyle = "#165dcc"
            ctx.roundRect(boxSize*x+boxSize//8, boxSize*y+boxSize//8, 3*boxSize//4, 3*boxSize//4, 3)
            ctx.closePath()
            ctx.fill()
            ctx.fillStyle = "#FFFFFF"
            ctx.font = "20px Arial"
            ctx.textAlign = "center"
            ctx.textBaseline = "middle"
            ctx.fillText(self._value, boxSize*x+boxSize//2,boxSize*y+boxSize//2)

    @property
    def value(self) -> int:
        return self._value
    @value.setter
    def value(self, value: int):
        if value < 0:
            raise ValueError("Box value has to be a nonnegative integer.")
        else:
            self._value = value 