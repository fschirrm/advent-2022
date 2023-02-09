import utils.utils as utils

c = utils.read_file("files/task3.txt")
priorities = 0
count = 0
while count < len(c):
    common_list = list(c[count][0])
    i = 1
    count += 1
    while (i<=2) and (count < len(c)):
        new_list =[]
        for m in range(len(common_list)):
            if (common_list[m] in c[count][0]) and not (common_list[m] in new_list): 
                new_list.append(common_list[m])
        common_list = new_list
        i += 1; count += 1
    if len(common_list) > 0: 
        if ord(common_list[0]) < 91: priorities += (ord(common_list[0]) - 38)
        else: priorities += (ord(common_list[0]) - 96)
print(f"Priorities: {priorities}")