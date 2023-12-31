import os
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
            print(f'cannot set the canvas at [{pos}]')

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Clear the terminal and then print each line in the canvas
    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))