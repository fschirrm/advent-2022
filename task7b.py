import utils.utils as utils

def sum_list(dir):
    sum_dir = 0
    size_array =[]
    for elem in dir[2]:
        if elem[0] == "f": sum_dir += elem[2]
        if elem[0] == "d": 
            add_dir, add_array = sum_list(elem)
            sum_dir += add_dir
            size_array += add_array
    size_array.insert(0,[dir[1], sum_dir])
    return sum_dir, size_array

c = utils.read_file("files/task7.txt")
dir_struct = ["d","/",[], None]
curr_dir = dir_struct
curr_command = ""
if (c[0][1] == "cd") and (c[0][2] == "/"): c.pop(0)
for list in c:
    if list[0] == "$":
        if list[1] == "ls":
            curr_command = "ls"
        if list[1] == "cd":
            found = False
            if list[2] == "..": 
                curr_dir = curr_dir[3]
            else:
                for elem in curr_dir[2]:
                    curr_command = "cd"
                    if (elem[0] == "d") and (elem[1] == list[2]):
                        curr_dir = elem
                        found = True
                        break
                if not found: print (f"Directory {list[2]} not found!")
    else:
        if curr_command == "ls":
            content = curr_dir[2]
            if (list[0] == "dir") and (list[1] != ".."): 
                content = curr_dir[2]
                name = list[1]
                content.append(["d",name,[],curr_dir])
            if list[0].isnumeric(): content.append(["f",list[1],int(list[0])])
            
sum_dir, size_array = sum_list(dir_struct)
needed_space = - (70000000 - sum_dir - 30000000)
size_array.sort(key=lambda x: x[1])
for elem in size_array:
    if elem[1] >= needed_space:
        print(f"delete directory \"{elem[0]}\" with size: {elem[1]} ")
        break