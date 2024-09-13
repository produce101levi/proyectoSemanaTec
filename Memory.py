"""Memory, puzzle game of number pairs."""

from random import shuffle
from turtle import addshape
from turtle import done
from turtle import onscreenclick
from turtle import ontimer
from turtle import shape
from turtle import stamp
from turtle import setup
from turtle import hideturtle
from turtle import tracer
from turtle import update
from turtle import clear
from turtle import goto
from turtle import up
from turtle import down
from turtle import color
from turtle import begin_fill
from turtle import forward
from turtle import left
from turtle import end_fill
from turtle import write
from freegames import path

"""Definition of global variables:
car stand for the image in the back
titles is the list of numbers and their duplicate for the couples
state acts as a boolean state indicating whether the tokens were selected
hide is the state that indicates whether the cell should show the image behind
tap_count is the amount of taps of the player
"""
car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
tap_count = 0


def check_win():
    """Check if the player has won the game to display mesage."""
    if all(not hidden for hidden in hide):
        up()
        goto(0, 0)
        color('green')      # Definition of text color
        # Share victory mesage
        write("¡Ganaste!", align="center", font=("Arial", 36, "bold"))
        return True  # Stop execution
    return False


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()        # Lift pen to move without drawing
    goto(x, y)      # Locate in start position
    down()      # Lower pen to start drawing
    color('black', 'white')     # Deff of used colors
    begin_fill()        # Start filling the scuare with white color
    for count in range(4):      # Draw the 4 sides of the scuare
        forward(50)
        left(90)
    end_fill()      # End the drawing and fill it


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Handle a screen tap event, update the tile state."""
    global tap_count        # Get the tap_counter variable
    spot = index(x, y)      # Get the index of the tile that was tapped
    mark = state['mark']        # Get the currently selected tile
    # Increase the tap count every time a tile is tapped
    tap_count += 1
    # If the action does not alter the state
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot        # Mark the tapped tile as selected
    else:
        # If tiles match, reveal both tiles
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None        # Reset the selected tile


def draw():
    """Draw image and tiles."""
    clear()     # Clear the window
    goto(0, 0)
    shape(car)      # Share the image
    stamp()     # Stampo the image in the window
    # Iterate through all 64 tiles
    for count in range(64):
        if hide[count]:     # If the tile is hidden
            x, y = xy(count)        # Get the (x, y) coordinates of the tile
            square(x, y)        # Draw a white square at the tile position
    mark = state['mark']        # Get the currently selected tile
    # If a tile is selected and still hidden
    if mark is not None and hide[mark]:
        x, y = xy(mark)     # Get the (x, y) coordinates of the selected tile
        up()
        goto(x + 2, y)      # Move slightly to adjust for text position
        color('black')      # Set text black
        # Display the tile number
        write(tiles[mark], font=('Arial', 30, 'normal'))
    up()
    check_win()     # Call check win
    goto(-180, 180)     # Position in the top left corner
    color('black')      # Set the text color to black
    # Display the number of taps
    write(f'Taps: {tap_count}', font=('Arial', 16, 'normal'))
    update()        # Refresh the screen with the new drawing
    ontimer(draw, 100)      # Call the draw function every 100 milliseconds


"""Use of fuctions so the game can start."""
shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
