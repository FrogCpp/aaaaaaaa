from CellClass import Cell as CC
import random as rand

class Board():
    def __init__(self, x=5, y=5):
        self._size = (x, y)
        self._mines = (self._size[0] * self._size[1]) // 10
        self._board = []
        self._massMines = []

        for i in range(x):
            line = []
            for j in range(y):
                obj = CC(_poz=(i, j))
                self._mines -= 1 if obj._isMine else 0
                line.append(obj)
            self._board.append(line)

        for i in range(self._mines):
            a = rand.randint(0, self._size[0]-1)
            b = rand.randint(0, self._size[1]-1)
            self._board[a][b]._isMine = True
            self._massMines.append(self._board[a][b])

        for i in range(x):
            for j in range(y):
                obj = self._board[i][j]
                for ii in range(i-1, i+2):
                    line = []
                    for jj in range(j-1, j+2):
                        try:
                            line.append(self._board[ii][jj] if ii >= 0 and jj >= 0 else None)
                        except:
                            pass
                    obj._supports.append(line)
                obj.complited()

        return

    def printing(self):
        print('  ', *list(range(self._size[1])), sep='\t')
        print()
        for line in self._board:
            print(self._board.index(line), '\t', end='')
            for symbol in line:
                print(symbol, end='\t')
            print()
        return

    def inputing(self, coords):
        x = coords[0]
        y = coords[1]
        self._board[x][y].Click(_mousClick=True)
        if self._board[x][y] in self._massMines:
            return False
        else:
            return True

    def IsEnd(self):
        counter = 0
        for line in self._board:
            for point in line:
                if point not in self._massMines and not point._status:
                    counter += 1
        return not counter == sum(list(map(len, self._board))) - len(self._massMines)


b = Board()