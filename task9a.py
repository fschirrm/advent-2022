import utils.utils as utils

moves = utils.read_file("files/task9.txt")
# print(moves)

field =[[False for x in range(2000)] for y in range(2000) ]
field[1000][1000] = True
h = [1000, 1000]
t = [1000, 1000]
for elem in moves:
    for i in range(int(elem[1])):
        if elem[0] == "U": h = [h[0] - 1, h[1]]
        if elem[0] == "D": h = [h[0] + 1, h[1]]
        if elem[0] == "L": h = [h[0], h[1] - 1]
        if elem[0] == "R": h = [h[0], h[1] + 1]
        if abs(h[0] - t[0]) > 1:
            if h[0] < t[0]: t = [t[0] - 1, t[1]]
            else: t = [t[0] + 1, t[1]]
            if h[1] < t[1]: t = [t[0], t[1] - 1]
            else: 
                if h[1] > t[1]: t = [t[0], t[1] + 1]
        else:
            if abs(h[1] - t[1]) > 1:
                
                if h[1] < t[1]: t = [t[0], t[1] - 1]
                else: t = [t[0], t[1] + 1]
                if h[0] < t[0]: t = [t[0] - 1, t[1]]
                else: 
                    if h[0] > t[0]: t = [t[0] + 1, t[1]]
        field[t[0]][t[1]] = True
number = 0
for list in field:
    for elem in list:
        if elem: number += 1

print(f"number of fields: {number}")