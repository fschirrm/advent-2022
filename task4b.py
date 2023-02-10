import utils.utils as utils

c = utils.read_file("files/task4.txt")
count = 0
for elem in c:
    sp = elem[0].split(',')
    l_range = sp[0].split('-')
    r_range = sp[1].split('-')
    if (int(l_range[0]) == int(r_range[0])) or (int(l_range[1]) == int(r_range[1])): count += 1
    else:
        if int(l_range[0]) < int(r_range[0]):
            if (int(l_range[1]) >= int(r_range[0])): count += 1
        else: 
            if int(l_range[0]) <= int(r_range[1]): count += 1
print(f"number of complete overlapping pairs: {count}")
               