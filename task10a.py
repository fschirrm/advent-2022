import utils.utils as utils

prog = utils.read_file("files/task10.txt")
x = 1
step = 20
step_40 = 0
s_strenght = 0
print(prog)
for elem in prog:
    if elem[0] == "noop": step += 1
    if elem[0] == "addx": step += 2
    if (step // 40) > step_40:
        step_40 += 1
        s_strenght += (((step - 20) // 10) * 10 * x)
    if elem[0] == "addx": x += int(elem[1])
    
print(f"sum signal strenght: {s_strenght}")  