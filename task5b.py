import utils.utils as utils

stacks, moves = utils.read_stacks("files/task5.txt")
for elem in moves:
    from_list = stacks[elem[1][0]]
    to_list = stacks[elem[1][1]]
    cache = []
    for i in range(elem[0]):
        cache.insert(0,from_list[0])
        from_list.pop(0)    
    for item in cache: to_list.insert(0,item)    
    stacks[elem[1][0]] = from_list
    stacks[elem[1][1]] = to_list
print("result: ", end='')
for item in stacks.values():
    print(item[0], end='')