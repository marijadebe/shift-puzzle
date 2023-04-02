from js import (
    document,
    console,
    window
    )
from static.Board import Board
from pyodide.ffi.wrappers import add_event_listener
import asyncio

canvas = document.getElementById("platno")
ctx = canvas.getContext("2d")
board = Board()
gameData = {
    "moves": 0,
    "time": 0,
    "gameEnd": False
}

def gameStart():
    resizeCanvas()
    board.shuffleSelf()
    board.drawSelf(canvas)

def canvasClickListener(evt):
    rect = canvas.getBoundingClientRect()
    doRedraw = board.clickHandler(evt.clientX -rect.left, evt.clientY- rect.top, canvas)
    if doRedraw:
        board.drawSelf(canvas)
        global gameData
        gameData["moves"] += 1
        output = f"Time: {gameData['time']// 60:02d}:{gameData['time']%60:02d}, Moves: {gameData['moves']}"
        document.getElementById("gameHead").innerHTML = output

def resizeCanvas(evt = None):
    if window.innerWidth > 1000:
        canvas.width = window.innerWidth//4
        canvas.height = window.innerWidth//4
    else:
        canvas.width = window.innerWidth//2
        canvas.height = window.innerWidth//2
    
    board.drawSelf(canvas)

async def timer():
    global gameData
    while not gameData['gameEnd']:
        await asyncio.sleep(1)
        gameData["time"] += 1
        output = f"Time: {gameData['time']// 60:02d}:{gameData['time']%60:02d}, Moves: {gameData['moves']}"
        document.getElementById("gameHead").innerHTML = output

gameStart()
add_event_listener(
    canvas,
    "click",
    canvasClickListener
)
add_event_listener(
    window,
    'resize',
    resizeCanvas
)
pyscript.run_until_complete(timer())