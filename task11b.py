import utils.utils as utils

rounds = 10000
c = utils.read_file("files/task11.txt") 
monkey_list = []
monkey = None

def operate(nr_list, op_list):
    new_nr_list = []
    for elem in nr_list:
        if op_list[0] == "old": z1 = elem
        else: z1 = int(op_list[0])
        if op_list[2] == "old": z2 = elem
        else: z2 = int(op_list[2])
        if op_list[1] == "*": new_nr_list.append(z1 * z2)
        else: new_nr_list.append(z1 + z2)
    return new_nr_list        
        
for line in c:
    if line[0] == "Monkey": 
        if not monkey == None: monkey_list.append(monkey)
        monkey = [[],[],[],0]
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
for monkey in monkey_list:
    for i in range(len(monkey[0])):
        monkey[0][i] = [monkey[0][i] for x in range(len(monkey_list))]
for i in range(rounds):
    for j in range(len(monkey_list)):
        for item in monkey_list[j][0]:
            monkey_list[j][3] += 1
            item = operate(item, monkey_list[j][1])
            for k in range(len(item)):
                item[k] = item[k] % monkey_list[k][2][0]
            if item[j] == 0: monkey_list[monkey_list[j][2][1]][0].append(item)
            else:  monkey_list[monkey_list[j][2][2]][0].append(item)
        monkey_list[j][0] = []
monkey_list.sort(key=lambda x: x[3], reverse=True)
business = monkey_list[0][3] * monkey_list[1][3]
print(f"business level: {business}")