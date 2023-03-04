import utils.utils as utils

c = utils.read_file("files/task12.txt") 
open_nodes = []
dij_field = []
start_node = []

def arrange_node(node):
    global open_nodes
    if len(open_nodes)==0: 
        open_nodes.append(node)
    else:
        if node['in_node_list']: open_nodes.remove(node)
        inserted=False
        for i in range(len(open_nodes)-1,-1,-1):
            if (node['len'] > open_nodes[i]['len']):
                node['in_node_list'] = True
                open_nodes.insert(i+1,node)
                inserted=True
                break
        if not inserted: 
            open_nodes.insert(0,node)
    node['in_node_list'] = True
    return

for i in range(len(c)):
    new_line=[]
    for j in range(len(c[i][0])):
        new_elem = {'pos': (i,j), 'in_node_list': False, 'pre': None, 'len': -1, 'finished': False, 'value':c[i][0][j], 'node_type': 'N'}
        if new_elem['value'] in ['S','a']:
            new_elem['value'] = 'a'
            start_node.append(new_elem)
        if new_elem['value'] == 'E':
            new_elem['node_type'] = 'E'
            new_elem['value'] = 'z'
        new_line.append(new_elem)
        # if c[i][0][j] == "S": 
        #     new_elem['len'] = 0
        #     new_elem['in_node_list'] = True
        #     open_nodes.append(new_elem)
    dij_field.append(new_line)
    
len_to_e = -1
while (len_to_e < 0 and len(open_nodes) > 0):
    curr_node = open_nodes.pop(0)
    curr_node['in_node_list'] == False
    curr_node['finished']=True
    if curr_node['node_type'] == "E":
        len_to_e = curr_node['len']
    else:
        n_pos=[(curr_node['pos'][0]-1, curr_node['pos'][1]), (curr_node['pos'][0], curr_node['pos'][1]-1),
        (curr_node['pos'][0]+1, curr_node['pos'][1]), (curr_node['pos'][0], curr_node['pos'][1]+1)]
        for elem in n_pos:
            if elem[0]>=0 and elem[0]<len(dij_field) and elem[1]>=0 and elem[1]<len(dij_field[0]):
                check_node = dij_field[elem[0]][elem[1]]
                if (not check_node['finished']):
                    if ord(curr_node['value']) + 1 >= ord(check_node['value']):
                        new_len = curr_node['len'] + 1
                        if (check_node['len'] < 0) or (new_len < check_node['len']):
                            check_node['len'] = new_len
                            check_node['pre']= curr_node
                            arrange_node(check_node)
                                                        
print (f"Result = {len_to_e}")
# while curr_node['node_type'] != "S": 
#     print (curr_node["value"],end = " "); print(curr_node["pos"])
#     curr_node = curr_node['pre']
