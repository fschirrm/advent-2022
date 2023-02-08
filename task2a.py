import utils.utils as utils

win_points = { "AX" : 3, "AY" : 6, "AZ" : 0, "BX" : 0, "BY" : 3, "BZ" : 6, "CX" : 6, "CY" : 0, "CZ" : 3 }
shape_points = {"X" : 1, "Y" : 2, "Z" : 3}
c = utils.read_file("files/task2.txt")
total_points = 0
for elem in c:
    total_points += shape_points[elem[1]]
    total_points += win_points[elem[0] + elem[1]]
print(f"whole points: {total_points}")