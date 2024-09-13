from turtle import (color, up, goto, down,
                    circle, setup, hideturtle, tracer,
                    update, onscreenclick, done)
from freegames import line


def grid():
    """Dibuja el tablero de tres en raya."""
    # Dibuja las dos líneas verticales
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    # Dibuja las dos líneas horizontales
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Dibuja el símbolo del jugador X en rojo."""
    color("red")  # Cambia el color a rojo para X
    # Dibuja las dos líneas que forman la X
    line(x + 20, y + 20, x + 113, y + 113)
    line(x + 20, y + 113, x + 113, y + 20)


def drawo(x, y):
    """Dibuja el símbolo del jugador O en azul."""
    up()  # Levanta el lápiz antes de moverlo
    goto(x + 67, y + 30)  # Posiciona el círculo en el centro de la celda
    down()  # Baja el lápiz para empezar a dibujar
    color("blue")  # Cambia el color a azul para O
    circle(50)  # Dibuja un círculo de radio 50


def floor(value):
    """
    Redondea el valor para alinearlo a la cuadrícula.
    La cuadrícula tiene cuadrados de tamaño 133x133.
    """
    return ((value + 200) // 133) * 133 - 200


# Diccionario para almacenar el estado del tablero
# Cada posición del tablero será una clave en este diccionario
board = {}


def tap(x, y):
    """
    Maneja el evento de hacer clic en el tablero.
    Dibuja una X o un O dependiendo del jugador y
    verifica si la casilla está ocupada.
    """
    # Alinea las coordenadas x, y al centro de una celda de la cuadrícula
    x = floor(x)
    y = floor(y)

    # Verifica si la casilla ya está ocupada
    if (x, y) in board:
        print("Casilla ya ocupada")
        return

    player = state['player']
    draw = players[player]
    draw(x, y)
    board[(x, y)] = player
    update()
    state['player'] = not player


# Estado del juego. Comienza con el jugador 0 (X)
state = {'player': 0}

players = [drawx, drawo]

# Configuración de la ventana
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
