def check_unique(s):
    unique = True
    for m in range(len(s)):
        for n in range(len(s)):
            if (m != n) and (s[m] == s[n]): 
                unique = False
                break
        if not unique: break
    return unique    

f = open("files/task6.txt","r")
line = f.readline().strip()
marker = 0
for i in range(14, len(line)):
    if check_unique(line[i-14:i]):
        marker = i
        break

print(f"marker: {marker}")