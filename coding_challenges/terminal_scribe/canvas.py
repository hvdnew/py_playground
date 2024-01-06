
from terminal_scribe_exceptions import TerminalScribeException, InvalidParameterException
from terminal_scribe import TerminalScribe, PlotTerminalScribe, RoboticTerminalScribe, RandomizedTerminalScribe
from threading import Thread
import time
import os

# a class to hold canvas state
class Canvas:
    # takes canvas dimention and initiates a blank canvas
    def __init__(self, x, y, scribes=[], framerate=0.005):
        self._x = x
        self._y = y
        # creating a X * Y 2D matrix (list of lists) to capture X * Y pixels of blank canvas
        # [ [col1], [col2].... [col3]]
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]
        self.scribes = scribes
        self.framerate = framerate

    def addScribe(self, terminalScribe):
        self.scribes.append(terminalScribe)

    def go(self):

        if(len(self.scribes) == 0):
            raise InvalidParameterException(f"cannot execute go on a canvas with no scribes")

        def _call_scribe_move(_canvas, _scribe):
            if len(_scribe.moves) > i:
                args = _scribe.moves[i][1] + [_canvas, _scribe]
                _scribe.moves[i][0](*args)

        print(f'==> {self.scribes}')

        max_moves = max([len(scribe.moves) for scribe in self.scribes])
        for i in range(0, max_moves):
            threads = [Thread(target=_call_scribe_move, args=[self, scribe]) for scribe in self.scribes]
            [thread.start() for thread in threads]
            [thread.join() for thread in threads]
            self.print()
            time.sleep(self.framerate)

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

    def toDict(self):
        return {
            'classname': type(self).__name__,
            'x': self._x,
            'y': self._y,
            'canvas': self._canvas,
            'scribes': [scribe.toDict() for scribe in self.scribes]
        }
    @classmethod
    def fromDict(self, data):
        canvas = globals()[data.get('classname')](
            data.get('x'), 
            data.get('y'), 
            [globals()[scribeDict.get('classname')].fromDict(scribeDict) for scribeDict in data.get('scribes')]
        )
        canvas._canvas = data.get('canvas')
        return canvas
