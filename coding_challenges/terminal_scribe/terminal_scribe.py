
from dataclasses import dataclass
import os
import time

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
        return point[0] < 0 or point[0] >= self._x or point[1] < 0 or point[1] >= self._y


    # draw 'mark' at a given coordinate on the canvss
    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark

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

    # 1. Draw a 'trail' char on the current pos, move to the next pos, and draw 'mark' char on that pos
    def draw(self, new_pos):
        self.canvas.setPos(self.pos, self.trail)
        self.pos = new_pos
        self.canvas.setPos(self.pos, self.mark)
        self.canvas.print()
        # Sleep for a little bit to create the animation
        time.sleep(self.delay)

    # move x coordinate by -1
    def drawLeft(self):
        leftPos = (self.pos[0]-1, self.pos[1])
        if not self.canvas.hitsWall(leftPos):
            self.draw(leftPos)

    # move x coordinate by +1
    def drawRight(self):
        rightPos = (self.pos[0]+1, self.pos[1])
        if not self.canvas.hitsWall(rightPos):
            self.draw(rightPos)

    # move y coordinate by -1
    def drawUp(self):
        upPos = (self.pos[0], self.pos[1]-1)
        if not self.canvas.hitsWall(upPos):
            self.draw(upPos)

    # move y coordinate by -1
    def drawDown(self):
        downPos = (self.pos[0], self.pos[1]+1)
        if not self.canvas.hitsWall(downPos):
            self.draw(downPos)

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

scribe.drawSquare(15)