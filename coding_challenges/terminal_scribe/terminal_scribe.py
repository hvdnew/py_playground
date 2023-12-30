
from dataclasses import dataclass
import os
import time
import math

# a class to hold canvas state
class Canvas:
    # takes canvas dimention and initiates a blank canvas
    def __init__(self, x, y):
        self._x = x
        self._y = y
        # creating a X * Y 2D matrix (list of lists) to capture X * Y pixels of blank canvas
        # [ [col1], [col2].... [col3]]
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]
        
    # Returns True if the given point is outside the boundaries of the Canvas
    def hitsWall(self, point):
        return round(point[0]) < 0 or round(point[0]) >= self._x or round(point[1]) < 0 or round(point[1]) >= self._y


    # draw 'mark' at a given coordinate on the canvss
    def setPos(self, pos, mark):
        self._canvas[round(pos[0])][round(pos[1])] = mark

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Clear the terminal and then print each line in the canvas
    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))


# a class to hold a canvas and 'scribe' on it, there is a trail and a mark
# mark shows current state and trail shows a visited coordiante
class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.pos = (0, 0)
        self.mark  = "*"
        self.trail = "."
        self.delay = 0.01
        # a feature to add a sense of direction in scribe
        # x is left (-1) or right (1), and y is up (-1) or down (1)
        self.direction = [0, 1]

    # adding degrees to direction makes it flexible to move into that angle.
    # formulae to devise next coordinate based on degree is taken from a LinkedIn course
    def setDegrees(self, degrees):
        radians = (degrees / 180) * math.pi
        self.direction = [math.sin(radians), -math.cos(radians)]

    # 1. Draw a 'trail' char on the current pos, move to the next pos, and draw 'mark' char on that pos
    def draw(self, new_pos):
        self.canvas.setPos(self.pos, self.trail)
        self.pos = new_pos
        self.canvas.setPos(self.pos, self.mark)
        self.canvas.print()
        # Sleep for a little bit to create the animation
        time.sleep(self.delay)

    def forward(self):
        next_pos = (self.pos[0] + self.direction[0], self.pos[1] + self.direction[1])
        if not self.canvas.hitsWall(next_pos):
            self.draw(next_pos)

    # move x coordinate by -1
    def drawLeft(self):
        self.direction = (-1, 0)
        self.forward()

    # move x coordinate by +1
    def drawRight(self):
        self.direction = (1, 0)
        self.forward()

    def drawUp(self):
        self.direction = (0, -1)
        self.forward()

    def drawDown(self):
        self.direction = (0, 1)
        self.forward()

    def drawSquare(self, square_size):

        for i in range(0, square_size):
            self.drawRight()

        for i in range(1, square_size):
            self.drawDown()

        for i in range(0, square_size):
            self.drawLeft()

        for i in range(1, square_size):
            self.drawUp()
        

canvas = Canvas(20, 20)
scribe = TerminalScribe(canvas)

scribe.setDegrees(135)

for i in range(20):
    scribe.forward()
