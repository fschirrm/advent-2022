import utils.utils as utils

c = utils.read_file("files/task8.txt")
visibility_list =[]
for list in c:
    row =[]
    for i in range(len(list[0])):
        row.append([int(list[0][i]), 0])
    visibility_list.append(row)

vis_big=0
for i in range(len(visibility_list)):
    for j in range(len(visibility_list[0])):
        vis = 0
        vis_all = 1
        for m in range(j+1,len(visibility_list[0])):
            vis += 1
            if visibility_list[i][j][0] <= visibility_list[i][m][0]: break
        if vis > 0: vis_all *= vis
        vis = 0
        for m in range(j-1,-1,-1):
            vis += 1
            if visibility_list[i][j][0] <= visibility_list[i][m][0]: break
        if vis > 0: vis_all *= vis 
        vis = 0
        for m in range(i+1,len(visibility_list)):
            vis += 1
            if visibility_list[i][j][0] <= visibility_list[m][j][0]: break
        if vis > 0: vis_all *= vis
        vis = 0
        for m in range(i-1,-1,-1):
            vis += 1
            if visibility_list[i][j][0] <= visibility_list[m][j][0]: break
        if vis > 0: vis_all *= vis
        visibility_list[i][j][1] = vis_all
        if vis_all > vis_big: vis_big = vis_all
print(f"biggest number is: {vis_big}")
