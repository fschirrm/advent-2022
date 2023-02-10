import utils.utils as utils

stacks, moves = utils.read_stacks("files/task5.txt")
for elem in moves:
    for i in range(elem[0]):
        from_list = stacks[elem[1][0]]
        to_list = stacks[elem[1][1]]
        to_list.insert(0,from_list[0])
        from_list.pop(0)
        stacks[elem[1][0]] = from_list
        stacks[elem[1][1]] = to_list
print("result: ", end='')
for item in stacks.values():
    print(item[0], end='')