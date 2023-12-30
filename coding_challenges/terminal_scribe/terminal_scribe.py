
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


    def hitsHorzWall(self, point):
        return round(point[0]) < 0 or round(point[0]) >= self._x   
    
    def hitsVertWall(self, point):
        return round(point[1]) < 0 or round(point[1]) >= self._y  
    
    def getReflection(self, point):
        return (-1 if self.hitsHorzWall(point) else 1, -1 if self.hitsVertWall(point) else 1)
    
    # Returns True if the given point is outside the boundaries of the Canvas
    def hitsWall(self, point):
        return self.hitsHorzWall(point) or self.hitsVertWall(point)


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

    def bounce(self, pos):
        reflection = self.canvas.getReflection(pos)
        self.direction = (self.direction[0] * reflection[0], self.direction[1] * reflection[1])


    def forward(self, distance=1):
        for i in range(distance):
            next_pos = (self.pos[0] + self.direction[0], self.pos[1] + self.direction[1])
            if self.canvas.hitsWall(next_pos):
                self.bounce(next_pos)
                next_pos = (self.pos[0] + self.direction[0], self.pos[1] + self.direction[1])
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
scribe = TerminalScribe(canvas=canvas)
scribe.setPos((4, 6))
scribe.setDegrees(150)
scribe.forward(1000)

# data structure to hold information to create and operate multiple scribes at once. 
# definition includes, name, position and instructions
# instructions are later flattened and executed for all the scribes 
# scribes = [
#     {
#         "name": "scribeZ",
#         "position": (7, 0),
#         "instructions": [
#             {
#                 "function": "left",
#                 "duration": 5
#             },
#             {
#                 "function": "down",
#                 "duration": 4
#             },
#             {
#                 "function": "right",
#                 "duration": 5
#             },
#             {
#                 "function": "up",
#                 "duration": 4
#             }
#         ]
#     },
#     {
#         "name": "scribeA",
#         "position": (5, 5),
#         "instructions": [
#             {
#                 "function": "forward",
#                 "duration": 10
#             }
#         ]
#     },
#     {
#         "name": "scribeB",
#         "position": (3, 10),
#         "instructions": [
#             {
#                 "function": "forward",
#                 "duration": 5
#             },
#             {
#                 "function": "down",
#                 "duration": 5
#             },
#             {
#                 "function": "right",
#                 "duration": 8
#             },
#             {
#                 "function": "up",
#                 "duration": 199
#             }
#         ]
#     }
# ]

# for scribeDefinition in scribes:
#     scribeDefinition['scribe'] = TerminalScribe(canvas=canvas)
#     scribeDefinition['scribe'].setPos(scribeDefinition['position'])

#     scribeDefinition['instructions_flat'] = []
#     for instruction in scribeDefinition['instructions']:
#         scribeDefinition['instructions_flat'] = scribeDefinition['instructions_flat'] + [instruction['function']] * instruction['duration']

# # find the longest instructions arr length
# maxInstructionLen = max([len(scribeDefinition['instructions_flat']) for scribeDefinition in scribes])

# # for counter execute all the scribes' instructions
# for i in range(0, maxInstructionLen):
#     for scribeDefinition in scribes:
#         if i < len(scribeDefinition['instructions_flat']):
#             fun_name = scribeDefinition['instructions_flat'][i]
#             if fun_name == 'forward':
#                 scribeDefinition['scribe'].forward()
#             elif fun_name == 'up':
#                 scribeDefinition['scribe'].drawUp()
#             elif fun_name == 'down':
#                 scribeDefinition['scribe'].drawDown()
#             elif fun_name == 'left':
#                 scribeDefinition['scribe'].drawLeft()
#             elif fun_name == 'right':
#                 scribeDefinition['scribe'].drawRight()
