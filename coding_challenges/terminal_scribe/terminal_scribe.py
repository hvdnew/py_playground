
from dataclasses import dataclass
import time
import math
import random
from inspect import getmembers, ismethod
from terminal_scribe_exceptions import TerminalScribeException, InvalidParameterException

class Scribe:
    def __init__(self) -> None:
        pass

# a class to hold a canvas and 'scribe' on it, there is a trail and a mark
# mark shows current state and trail shows a visited coordiante
class TerminalScribe(Scribe):
    def __init__(self, pos=(0,0), mark="*", trail=".", delay=0.01, direction=(0,1)):
        self.validate(pos, mark, trail, delay, direction)
        self.pos = pos
        self.mark  = mark
        self.trail = trail
        self.delay = delay
        # a feature to add a sense of direction in scribe
        # x is left (-1) or right (1), and y is up (-1) or down (1)
        self.direction = direction
        self.moves = []
        self.override_param_direction = False

    def validate(self, pos, mark, trail, delay, direction):
        # validate pos
        if not pos or len(pos) != 2 or type(pos[0]) != int or type(pos[1]) != int:
            raise InvalidParameterException(f"Invalid pos parameter {pos} passed to a TerminalScribe constructor")  
        
        if len(str(mark)) != 1 or mark == trail:
            raise InvalidParameterException(f"mark {mark} should be at most 1 char long and should not be same as trail {trail}")
        
        if len(str(trail)) != 1:
            raise InvalidParameterException(f"trail {trail} should be at most 1 char long")
        
        if type(delay) != float or float(delay) > 5.0:
            raise InvalidParameterException(f"delay {delay} should be a float and less than 5")
        
        if len(direction) != 2 or type(direction[0]) != int or type(direction[1]) != int:
            raise InvalidParameterException(f"Invalid direction parameter {direction} passed to a TerminalScribe constructor")


    def setPos(self, pos):
        self.pos = pos

    # adding degrees to direction makes it flexible to move into that angle.
    # formulae to devise next coordinate based on degree is taken from a LinkedIn course
    def setDegrees(self, degrees):
        radians = (degrees / 180) * math.pi
        self.direction = [math.sin(radians), -math.cos(radians)]

    # 1. Draw a 'trail' char on the current pos, move to the next pos, and draw 'mark' char on that pos
    def draw(self, new_pos, canvas):
        canvas.setPos(self.pos, self.trail)
        self.pos = new_pos
        canvas.setPos(self.pos, self.mark)
        canvas.print()
        # Sleep for a little bit to create the animation
        #time.sleep(self.delay)


    # bound when hit a wal using a reflection from the canvas state
    def bounce(self, pos, canvas):
        reflection = canvas.getReflection(pos)
        self.direction = (self.direction[0] * reflection[0], self.direction[1] * reflection[1])

    def bounceOffDirection(self, pos, direction, canvas):
        reflection = canvas.getReflection(pos)
        self.direction = (direction[0] * reflection[0], direction[1] * reflection[1])

    def _forward(self, scribe_direction, canvas, term_scribe):
            effective_scribe_direction = term_scribe.direction if term_scribe.override_param_direction else scribe_direction
            next_pos = (term_scribe.pos[0] + effective_scribe_direction[0], term_scribe.pos[1] + effective_scribe_direction[1])
             
            if canvas.hitsWall(next_pos):
                # print(f"bouncing from pos {next_pos}, term_scribe.pos {term_scribe.pos}, direction {effective_scribe_direction} reflection {canvas.getReflection(next_pos)}")
                term_scribe.bounceOffDirection(next_pos, effective_scribe_direction, canvas)
                term_scribe.override_param_direction = True
                next_pos = (term_scribe.pos[0] + term_scribe.direction[0], term_scribe.pos[1] + term_scribe.direction[1])
                # print(f"to pos direction term_scribe.pos {term_scribe.pos} {self.direction} {next_pos}")
                # time.sleep(2)
            term_scribe.draw(next_pos, canvas)

    # move forward distance times
    def forward(self, distance=1):

        for i in range(distance):
            self.moves.append((self._forward, [self.direction]))

    def toDict(self):
        return {
            'classname': type(self).__name__,
            'mark': self.mark,
            'trail': self.trail,
            'pos': self.pos,
            'moves': [[move[0].__name__, move[1]] for move in self.moves]
        }
    
    @classmethod
    def fromDict(self, data):

        scribe = globals()[data.get('classname')](
            pos=data.get('pos'),
            mark=data.get('mark'),
            trail=data.get('trail')
        )
        scribe.moves = scribe._movesFromDict(data.get('moves'))
        return scribe;

    def _movesFromDict(self, movesData):
        bound_methods = {key: val for key, val in getmembers(self, predicate=ismethod)}
        return [[bound_methods[name], args] for name, args in movesData]

# special terminal scribe that takes forward direction in random directions
class PlotTerminalScribe(TerminalScribe):
    def __init__(self, pos=[0,0], mark="*", trail="."):
        super().__init__(pos=pos, mark=mark, trail=trail)

    def plotX(self, higherOrderFunction):
        for x in range(self.canvas._x):
            # calling the function to determine y point for a given x
            pos = (x, higherOrderFunction(x))
            if pos[1] and not self.canvas.hitsWall(pos):
                self.draw(pos)

# special terminal scribe that takes forward direction in random directions
class RandomizedTerminalScribe(TerminalScribe):
    def __init__(self, pos=[0,0], mark="*", trail=".", degree=90):
        super().__init__(pos=pos, mark=mark, trail=trail)
        self.random_degree = degree

    # bound when hit a wal using a reflection from the canvas state
    def bounce(self, pos, canvas):
        reflection = canvas.getReflection(pos)
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
    def __init__(self, pos=[0,0], mark="*", trail="."):
        super().__init__(pos=pos, mark=mark, trail=trail)

    # move x coordinate by -1
    def drawLeft(self, distance=1):
        self.direction = (-1, 0)
        # print(f'drawLeft {self.pos} {(self.pos[0] + self.direction[0], self.pos[1] + self.direction[1])}')
        self.forward(distance=distance)

    # move x coordinate by +1
    def drawRight(self, distance=1):
        self.direction = (1, 0)
        # print('drawRight')
        self.forward(distance=distance)

    def drawUp(self, distance=1):
        self.direction = (0, -1)
        # print('drawUp')
        self.forward(distance=distance)

    def drawDown(self, distance=1):
        self.direction = (0, 1)
        # print('drawDown')
        self.forward(distance=distance)

    def drawSquare(self, square_size):
        self.drawRight(square_size)
        self.drawDown(square_size)
        self.drawLeft(square_size)
        self.drawUp(square_size)