
from dataclasses import dataclass
import time
import math
import random
from canvas import Canvas



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

    def setPos(self, pos):
        self.pos = pos

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


    # bound when hit a wal using a reflection from the canvas state
    def bounce(self, pos):
        reflection = self.canvas.getReflection(pos)
        self.direction = (self.direction[0] * reflection[0], self.direction[1] * reflection[1])

    # move forward distance times
    def forward(self, distance=1):
        for i in range(distance):
            next_pos = (self.pos[0] + self.direction[0], self.pos[1] + self.direction[1])
            if self.canvas.hitsWall(next_pos):
                # str = f'hit wall at {next_pos}, reflection {self.canvas.getReflection(next_pos)}, current dir {self.direction}'
                self.bounce(next_pos)
                next_pos = (self.pos[0] + self.direction[0], self.pos[1] + self.direction[1])
                # print(f'{str} new next_pos {next_pos}, new direction {self.direction}')
                # time.sleep(2)
            self.draw(next_pos)

# special terminal scribe that takes forward direction in random directions
class PlotTerminalScribe(TerminalScribe):
    def __init__(self, canvas):
        super().__init__(canvas)

    def plotX(self, higherOrderFunction):
        for x in range(self.canvas._x):
            # calling the function to determine y point for a given x
            pos = (x, higherOrderFunction(x))
            if pos[1] and not self.canvas.hitsWall(pos):
                self.draw(pos)

# special terminal scribe that takes forward direction in random directions
class RandomizedTerminalScribe(TerminalScribe):
    def __init__(self, canvas, degree=90):
        super().__init__(canvas)
        self.random_degree = degree

    # bound when hit a wal using a reflection from the canvas state
    def bounce(self, pos):
        reflection = self.canvas.getReflection(pos)
        if reflection[0] == -1:
            self.random_degree = 360 - self.random_degree
        if reflection[-1] == -1:
            self.random_degree = 180 - self.random_degree
        self.direction = (self.direction[0] * reflection[0], self.direction[1] * reflection[1])

    def randomizeDegOrientation(self):
        self.random_degree = random.randrange(self.random_degree-10, self.random_degree+10)
        self.setDegrees(self.random_degree)


    def forward(self, distance=1):
        for i in range(distance):
            self.randomizeDegOrientation()
            super().forward()

# specialized TerminalScribe that has up, down, left, right methods, also it can draw a square
class RoboticTerminalScribe(TerminalScribe):
    def __init__(self, canvas):
        super().__init__(canvas)

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