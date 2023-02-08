import utils.utils as utils

c = utils.read_file("files/task1.txt")
biggest_num_field = [0,0,0]
curr_num = 0
for elem in c:
    if elem[0].isnumeric(): curr_num += int(elem[0])
    else:
        if curr_num > biggest_num_field[0]: 
            biggest_num_field[0] = curr_num
            biggest_num_field.sort()
        curr_num = 0
biggest_num = 0
for elem in biggest_num_field:
    biggest_num += elem
print (f"Biggest Number = {biggest_num}") 
    