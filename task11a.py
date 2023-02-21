import utils.utils as utils

rounds = 20
c = utils.read_file("files/task11.txt") 
monkey_list = []
monkey = None

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
#print(monkey_list)

for i in range(rounds):
    for monkey in monkey_list:
        for item in monkey[0]:
            monkey[3] += 1
            if monkey[1][0] == "old": z1 = item
            else: z1 = int(monkey[1][0])
            if monkey[1][2] == "old": z2 = item
            else: z2 = int(monkey[1][2])
            if monkey[1][1] == "*": new_item = z1 * z2
            else: new_item = z1 + z2
            new_item = new_item // 3
            if new_item % monkey[2][0] == 0: monkey_list[monkey[2][1]][0].append(new_item)
            else:  monkey_list[monkey[2][2]][0].append(new_item)
        monkey[0] = []
#print()
#print(monkey_list)
monkey_list.sort(key=lambda x: x[3], reverse=True)
business = monkey_list[0][3] * monkey_list[1][3]
print(f"business level: {business}")