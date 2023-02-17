import utils.utils as utils

moves = utils.read_file("files/task9.txt")
field =[[False for x in range(2000)] for y in range(2000) ]
field[1000][1000] = True
snake = [[1000, 1000] for x in range(10)]

for elem in moves:
    for i in range(int(elem[1])):
        if elem[0] == "U": snake[0] = [snake[0][0] - 1, snake[0][1]]
        if elem[0] == "D": snake[0] = [snake[0][0] + 1, snake[0][1]]
        if elem[0] == "L": snake[0] = [snake[0][0], snake[0][1] - 1]
        if elem[0] == "R": snake[0] = [snake[0][0], snake[0][1] + 1]
        for m in range(1,10):
            if abs(snake[m-1][0] - snake[m][0]) > 1:
                if snake[m-1][0] < snake[m][0]: snake[m] = [snake[m][0] - 1, snake[m][1]]
                else: snake[m] = [snake[m][0] + 1, snake[m][1]]
                if snake[m-1][1] < snake[m][1]: snake[m] = [snake[m][0], snake[m][1] - 1]
                else: 
                    if snake[m-1][1] > snake[m][1]: snake[m] = [snake[m][0], snake[m][1] + 1]
            else:
                if abs(snake[m-1][1] - snake[m][1]) > 1:
                    
                    if snake[m-1][1] < snake[m][1]: snake[m] = [snake[m][0], snake[m][1] - 1]
                    else: snake[m] = [snake[m][0], snake[m][1] + 1]
                    if snake[m-1][0] < snake[m][0]: snake[m] = [snake[m][0] - 1, snake[m][1]]
                    else: 
                        if snake[m-1][0] > snake[m][0]: snake[m] = [snake[m][0] + 1, snake[m][1]]
        field[snake[9][0]][snake[9][1]] = True
number = 0
for list in field:
    for elem in list:
        if elem: number += 1
print(f"number of fields: {number}")