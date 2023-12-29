
from dataclasses import dataclass
import os

# class to hold canvas state
class Canvas:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        # creating a X * Y 2D matrix
        self._canvas = [['' for y in range(self._y)] 
                        for x in range(self._x)]

    # draw 'mark' at a given coordinate on the canvss
    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))



class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.pos = (0, 0)
        self.mark  = "*"
        self.trail = "."

    #
    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)
        self.pos = pos
        self.canvas.setPos(self.pos, self.mark)
        self.canvas.print()

canvas = Canvas(20, 20)
scribe = TerminalScribe(canvas)

for i in range(0, 20):
    for j in range(i, 20):
        scribe.draw((i, j))