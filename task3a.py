import utils.utils as utils

c = utils.read_file("files/task3.txt")
priorities = 0
for elem in c:
    l = len(elem[0])
    s1 = elem[0][0:l//2]
    s2 = elem[0][l//2:]
    for entity in s2:
        if entity in s1:  
            if ord(entity) < 91: priorities += (ord(entity) - 38)
            else: priorities += (ord(entity) - 96)
            break
print(f"Priorities: {priorities}")