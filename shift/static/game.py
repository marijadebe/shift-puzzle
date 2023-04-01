from js import (
    document,
    console
    )
from static.Board import Board
import asyncio

canvas = document.getElementById("platno")
ctx = canvas.getContext("2d")
board = Board()
data = {
    "moves": 0,
    "time": 0,
    "gameEnd": False
}

def gameStart():
    board.drawSelf(canvas)

async def timer():
    while True:
        await asyncio.sleep(1)
        console.log("neco")
        data.time += 1
        output = f"Time: {data.time}, Moves: {data.moves}"
        Element("gameHead").write(output)

gameStart()