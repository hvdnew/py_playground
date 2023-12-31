
from dataclasses import dataclass
import time
import math
import random
import os


class TerminalScribeException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class InvalidParameter(TerminalScribeException):
    pass

# a class to hold canvas state
class Canvas:
    # takes canvas dimention and initiates a blank canvas
    def __init__(self, x, y):
        self._x = x
        self._y = y
        # creating a X * Y 2D matrix (list of lists) to capture X * Y pixels of blank canvas
        # [ [col1], [col2].... [col3]]
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]


    def hitsHorzWall(self, point):
        return round(point[1]) < 0 or round(point[1]) >= self._y   
    
    def hitsVertWall(self, point):
        return round(point[0]) < 0 or round(point[0]) >= self._x  
    
    def getReflection(self, point):
        return (-1 if self.hitsVertWall(point) else 1, -1 if self.hitsHorzWall(point) else 1)
    
    # Returns True if the given point is outside the boundaries of the Canvas
    def hitsWall(self, point):
        return self.hitsHorzWall(point) or self.hitsVertWall(point)


    # draw 'mark' at a given coordinate on the canvss
    def setPos(self, pos, mark):
        try:
            self._canvas[round(pos[0])][round(pos[1])] = mark
        except IndexError as e:
            raise TerminalScribeException(f'cannot set mark {mark} at the canvas at pos [{pos}]')

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
    def __init__(self, canvas, pos=(0,0), mark="*", trail=".", delay=0.01, direction=(0,1)):
        self.validate(pos, mark, trail, delay, direction)
        self.canvas = canvas
        self.pos = pos
        self.mark  = mark
        self.trail = trail
        self.delay = delay
        # a feature to add a sense of direction in scribe
        # x is left (-1) or right (1), and y is up (-1) or down (1)
        self.direction = direction

    def validate(self, pos, mark, trail, delay, direction):
        # validate pos
        if len(pos) != 2 or type(pos[0]) != int or type(pos[1]) != int:
            raise InvalidParameter(f"Invalid pos parameter {pos} passed to a TerminalScribe constructor")  
        
        if len(str(mark)) != 1 or mark == trail:
            raise InvalidParameter(f"mark {mark} should be at most 1 char long and should not be same as trail {trail}")
        
        if len(str(trail)) != 1:
            raise InvalidParameter(f"trail {trail} should be at most 1 char long")
        
        if type(delay) != float or float(delay) > 5.0:
            raise InvalidParameter(f"delay {delay} should be a float and less than 5")
        
        if len(direction) != 2 or type(direction[0]) != int or type(direction[1]) != int:
            raise InvalidParameter(f"Invalid direction parameter {direction} passed to a TerminalScribe constructor")


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