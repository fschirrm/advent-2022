import utils.utils as utils

c = utils.read_file("files/task1a.txt")
biggest_num = 0
curr_num = 0
for elem in c:
    if elem[0].isnumeric(): curr_num += int(elem[0])
    else:
        if curr_num > biggest_num: biggest_num = curr_num
        curr_num = 0
print (f"Biggest number = {biggest_num}") 
    

