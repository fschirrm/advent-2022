import utils.utils as utils

def set_sprite(x, row, row_count, screen, number_steps):
    for i in range(number_steps):
        if row_count in range(x-1, x+2): screen[row][row_count] = "#"
        else: screen[row][row_count] = "."
        if row_count == 39:
            row_count = 0
            if row == 5: row = 0
            else: row += 1
        else: row_count += 1
    return row, row_count, screen 

prog = utils.read_file("files/task10.txt")
x = 1
row_count = 0
row = 0
screen =[["." for x in range(40)] for y in range(6)]
for elem in prog:
    if elem[0] == "noop": 
        row, row_count, screen = set_sprite(x, row, row_count, screen, 1)
    if elem[0] == "addx": 
        row, row_count, screen = set_sprite(x, row, row_count, screen, 2)
        x += int(elem[1])
    
for list in screen:
    print()
    for chr in list: print(chr, end=" ")