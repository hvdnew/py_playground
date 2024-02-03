from itertools import product

# back tracking
class Sudoku:

    def print_sudoku(self, puzzle):

        puzzle = [['*' if num == 0 else num for num in row] for row in puzzle]
        print()
        for row in range(0, 9):
            if row%3 == 0 and row != 0:
                print('-' * 33)
            for col in range(0, 9):
                if col%3 == 0 and col != 0:
                    print(' | ', end='')
                print(f' {puzzle[row][col]} ', end='')
            print()
        print()

    def solve_sudoku(self, puzzle):

        for (row, col) in product(range(0, 9), repeat=2):
            if puzzle[row][col] == 0: # unassigned cell
                for num in range(1, 10):
                    allowed = True # check if the num is allowed in row/cell box
                    for i in range(0, 9):
                        if num in (puzzle[i][col], puzzle[row][i]): 
                            allowed = False # found in row or column, cannot use this number 
                            break;
                    for (i, j) in product(range(0, 3), repeat=2):
                        if puzzle[row - row%3 +i][col - col%3 + i] == num:
                            allowed = False # found in 3*3 box
                            break;
                    if allowed:
                        puzzle[row][col] = num
                        if trail := self.solve_sudoku(puzzle):
                            return trail
                        puzzle[row][col] = 0
                return False
        
        return puzzle

if __name__ == '__main__':
    puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
              [6, 0, 0, 1, 9, 5, 0, 0, 0],
              [0, 9, 8, 0, 0, 0, 0, 6, 0],
              [8, 0, 0, 0, 6, 0, 0, 0, 3],
              [4, 0, 0, 8, 0, 3, 0, 0, 1],
              [7, 0, 0, 0, 2, 0, 0, 0, 6],
              [0, 6, 0, 0, 0, 0, 2, 8, 0],
              [0, 0, 0, 4, 1, 9, 0, 0, 5],
              [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    sudoku = Sudoku()
    sudoku.print_sudoku(puzzle)
    sudoku.solve_sudoku(puzzle)
    sudoku.print_sudoku(puzzle)