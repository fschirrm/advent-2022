import utils.utils as utils

c = utils.read_file("files/task8.txt")
#print(c)
visibility_list =[]
for list in c:
    row =[]
    for i in range(len(list[0])):
        row.append([int(list[0][i]), False])
    visibility_list.append(row)
for list in visibility_list:
    high = -1
    for i in range (len(list)):
        if list[i][0] > high:
            list[i][1] = True
            high = list[i][0]
    high = -1
    for i in range (len(list)-1, -1, -1):
        if list[i][0] > high:
            list[i][1] = True
            high = list[i][0]
for i in range (len(visibility_list[0])):
    high = -1
    for j in range(len(visibility_list)):
        if visibility_list[j][i][0] > high:
            visibility_list[j][i][1] = True
            high = visibility_list[j][i][0]
    high = -1
    for j in range(len(visibility_list)-1, -1, -1):
        if visibility_list[j][i][0] > high:
            visibility_list[j][i][1] = True
            high = visibility_list[j][i][0]
    visibility_number = 0        
    for list in visibility_list:
        for elem in list:
            if elem[1]: visibility_number += 1
print(f"{visibility_number} trees are visible")
