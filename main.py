from Chess_Figures import Chess_Figures
import os.path
from os import path

#input = "Data.txt"
input = "Data1.txt"
output = "Output.txt"

if path.exists(output):
    import os
    os.remove(output)

tests = {}
with open(input, "r") as chess_data:
  T_cases = int(chess_data.readline())
  for line in chess_data:
      spliter = line.split(' ')
      number, figure, row, column = [i.strip() for i in spliter]
      piece = Chess_Figures(number, figure, row, column)
      tests[number] = piece
chess_data.close()

values = []
list = []
for each_key in tests:
    if tests[each_key].figure == 'r' or tests[each_key].figure == "Q":
        list = Chess_Figures.Max_Rook_Queen(int(tests[each_key].row), int(tests[each_key].column))
    elif tests[each_key].figure == "k":
        list = Chess_Figures.Max_Knight(int(tests[each_key].row), int(tests[each_key].column))
    elif tests[each_key].figure == "Q":
        list = Chess_Figures.Max_Rook_Queen(int(tests[each_key].row), int(tests[each_key].column))
    else:
        list = Chess_Figures.Max_Kings(int(tests[each_key].row), int(tests[each_key].column))
    values.append(list)

print(values)

with open(output, "w") as file:
        for answers in values:
            file.write("max amount on board: " + '%s\n' % answers)

file.close()