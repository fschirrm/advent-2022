import utils.utils as utils

win_dict = { "AX" : "C", "AY" : "A", "AZ" : "B", "BX" : "A", "BY" : "B", "BZ" : "C", "CX" : "B", "CY" : "C", "CZ" : "A" }
shape_points = {"A" : 1, "B" : 2, "C" : 3}
game_points = {"X" : 0, "Y" : 3, "Z" : 6}
c = utils.read_file("files/task2.txt")
total_points = 0
for elem in c:
    total_points += game_points[elem[1]]
    total_points += shape_points[win_dict[elem[0] + elem[1]]]
print(f"whole points: {total_points}")