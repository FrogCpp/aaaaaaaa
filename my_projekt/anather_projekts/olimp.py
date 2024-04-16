class Table:
    def __init__(self, row=1, col=1):
        self.row = row
        self.col = col
        self.table = [[0 for y in range(col)] for x in range(row)]

    def get_value(self, row=1, col=1):
        return self.table[row][col] if 0 <= row < self.row and 0 <= col < self.col else None

    def set_value(self, row=1, col=1, val=0):
        self.table[row][col] = val

    def n_rows(self):
        return self.row

    def n_cols(self):
        return self.col

    def delete_row(self, row=1):
        if 0 <= row < self.row:
            self.table.pop(row)
        self.row -= 1

    def delete_col(self, col=1):
        last_mass = []
        if 0 <= col < self.col:
            for i in self.table:
                i.pop(col)
            last_mass.append(i)
        self.table = last_mass
        self.col -= 1

    def add_row(self, row=1):
        if len(self.table) <= row:
            self.table.append(list(map(int, ('0 ' * self.col).split())))
        else:
            self.table.insert(row, list(map(int, ('0 ' * self.col).split())))
        self.row += 1

    def add_col(self, col=1):
        if col > self.col:
            new_table = []
            for i in self.table:
                new_table.append(i.append(0))
        else:
            new_table = self.table
            for i in self.table:
                new_table.insert(col, 0)
            self.table = new_table