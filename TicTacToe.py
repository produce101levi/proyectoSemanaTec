from turtle import (color, up, goto, down,
                    circle, setup, hideturtle, tracer,
                    update, onscreenclick, done)
from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    color("red")
    line(x + 20, y + 20, x + 113, y + 113)
    line(x + 20, y + 113, x + 113, y + 20)


def drawo(x, y):
    """Draw O player."""
    up()
    goto(x + 67, y + 30)
    down()
    color("blue")
    circle(50)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


board = {}


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    if (x, y) in board:
        print("Casilla ya ocupada")
        return

    player = state['player']
    draw = players[player]
    draw(x, y)
    board[(x, y)] = player
    update()
    state['player'] = not player


state = {'player': 0}
players = [drawx, drawo]

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
