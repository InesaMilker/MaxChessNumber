class Chess_Figures:
    def __init__(self, number, figure, row, column):
        self.number = number
        self.figure = figure
        self.row = row
        self.column = column

    def Max_Rook_Queen(row, collumn):
        amount = 0
        while row >= 0 and collumn >= 0:
            amount += 1
            collumn -= 1
            row -= 1
        print(amount)
        return amount

    def Max_Knight(row, collumn):
        amount = int((row * collumn)/2)
        print(amount)
        return amount

    def Max_Kings(row, collumn):
        amount = int((row + 1) / 2) * int((collumn + 1) / 2)
        print(amount)
        return amount