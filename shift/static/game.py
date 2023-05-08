from js import (
    document,
    console,
    window
)
from pyodide.ffi.wrappers import add_event_listener
from pyodide.ffi.wrappers import remove_event_listener
import asyncio

"""Metadata hry"""
boardSize = int(window.location.pathname.split("/").pop())
console.log(boardSize)
canvas = document.getElementById("platno")
ctx = canvas.getContext("2d")
screen = document.getElementById("gameOver")
board = Board(boardSize)
gameData = {
    "moves": 0,
    "time": 0,
    "gameEnd": False
}

def gameStart():
    """Procedura volana po nacteni okna."""
    resizeCanvas()
    board.shuffleSelf()
    board.drawSelf(canvas)

def gameStop():
    global gameData
    gameData['gameEnd'] = True
    remove_event_listener(canvas, 'click', canvasClickListener)
    remove_event_listener(window, 'keydown', windowKeyListener)
    screen.style.visibility = 'visible'
    message=f"<i class='bi bi-trophy-fill'></i><br/>You have won.<br/> Final time: {gameData['time'] // 60:02d}:{gameData['time']%60:02d}<br/> # of moves: {gameData['moves']}<a href='/'>Main menu.</a>"
    screen.innerHTML = message

def reDraw():
    """Prekresli metadata a hraci plochu po provedeni tahu"""
    board.drawSelf(canvas)
    global gameData
    gameData["moves"] += 1
    output = f"Time: {gameData['time'] // 60:02d}:{gameData['time']%60:02d}, Moves: {gameData['moves']}"
    document.getElementById("gameHead").innerHTML = output
    if board.isInWonState(): gameStop()

def canvasClickListener(evt):
    """Zachyceni kliknuti na hraci plochu.

    Args:
        evt (Object): Event data.
    """
    rect = canvas.getBoundingClientRect()
    doRedraw = board.clickHandler(evt.clientX -rect.left, evt.clientY- rect.top, canvas)
    if doRedraw: reDraw()    
def windowKeyListener(evt):
    """Zachyceni klaves pri fokusovani okna.

    Args:
        evt (Object): Event data.
    """
    doRedraw = False
    match evt.key:
        case "ArrowLeft": doRedraw = board.keyHandler(1,0,canvas)
        case "ArrowRight": doRedraw = board.keyHandler(-1,0,canvas)
        case "ArrowUp": doRedraw = board.keyHandler(0,1,canvas)
        case "ArrowDown": doRedraw = board.keyHandler(0,-1,canvas)
    if doRedraw: reDraw()

def resizeCanvas(evt = None):
    """Zachyceni zmeny velikosti okna. Zajistuje jistou responsivnost platna.

    Args:
        evt (Object, optional): Event data. Defaultne None.
    """
    if window.innerWidth > 1000:
        canvas.width = window.innerWidth//4
        canvas.height = window.innerWidth//4
    else:
        canvas.width = window.innerWidth//2
        canvas.height = window.innerWidth//2
    
    board.drawSelf(canvas)

async def timer():
    """Pocitadlo neustale ozivovane event loopem (simulace samostatneho vlakna).
    """
    global gameData
    while not gameData['gameEnd']:
        gameData["time"] += 1
        output = f"Time: {gameData['time']// 60:02d}:{gameData['time']%60:02d}, Moves: {gameData['moves']}"
        document.getElementById("gameHead").innerHTML = output
        await asyncio.sleep(1)

gameStart()
add_event_listener(
    canvas,
    "click",
    canvasClickListener
)
add_event_listener(
    window,
    "keydown",
    windowKeyListener
)
add_event_listener(
    window,
    'resize',
    resizeCanvas
)
pyscript.run_until_complete(timer())