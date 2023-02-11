f = open("files/task6.txt","r")
line = f.readline().strip()
marker = 0
for i in range(3, len(line)):
    if (line[i] != line[i-1]) and (line[i] != line[i-2]) and (line[i] != line[i-3]):
        if (line[i-1] != line[i-2]) and (line[i-1] != line[i-3]) and (line[i-2] != line[i-3]):
            marker = i + 1
            break
print(f"marker: {marker}")
               
