import utils.utils as utils

rounds = 20
c = utils.read_file("files/task11_test.txt")
print(c)  
monkey_list = []
monkey = None

for line in c:
    if line[0] == "Monkey": 
        if not monkey == None: monkey_list.append(monkey)
        monkey = [[],[],[]]
    if line[0] == "Starting":
        items = []
        for i in range(2,len(line)): 
            nr = line[i].replace(",","")
            items.append(int(nr))
        monkey[0] = items
    if line[0] == "Operation:": monkey[1] = [line[3], line[4], line[5]]
    if line[0] == "Test:": monkey[2] = [int(line[3]), -1, -1]
    if line[0] == "If":
        if line[1] == "true:": monkey[2][1] = int(line[5])
        if line[1] == "false:": monkey[2][2] = int(line[5])
monkey_list.append(monkey)
print()
print(monkey_list)