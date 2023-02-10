def read_file(f):
    with open(f) as f:
        content = [line.strip().split(" ") for line in f.readlines()]
    return content

def read_comma_list(f):
    with open(f) as f:
        content = f.readline()
    return [int(x) for x in content.split(",")]

def read_stacks(f):
    with open(f) as f:
        raw_stacks = []
        end_stacks = False
        while not end_stacks:
            line = f.readline()
            if line[1] == '1': end_stacks = True
            else: raw_stacks.append(line)
        stack_dict = {}
        for i in range(len(line)):
            if line[i].isdigit():
                new_stack = []
                for elem in raw_stacks:
                    if (len(elem) > i) and (elem[i-1] == '['): new_stack.append(elem[i]) 
                stack_dict[line[i]] = new_stack  
        line = f.readline()
        moves = []
        while line:
            line = f.readline()
            if line != '':
                l1 = line.split("from")
                num_str = l1[0].split(" ")[1]
                from_str = l1[1].split(" ")[1]
                to_str = l1[1].split(" ")[3].strip()                      
                moves.append([int(num_str), [from_str,to_str]])
    return stack_dict, moves