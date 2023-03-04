import utils.utils as utils

c = utils.read_file("files/task12.txt") 
dij_field = []
start_nodes = []

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
            start_nodes.append(new_elem)
        if new_elem['value'] == 'E':
            new_elem['node_type'] = 'E'
            new_elem['value'] = 'z'
        new_line.append(new_elem)
    dij_field.append(new_line)

result = -1
for start_node in start_nodes:
    for line in dij_field:
        for c_node in line:
            c_node['len'] = -1; c_node['pre'] = None; c_node['finished'] = False; c_node['in_node_list'] = False
    start_node['node_type'] = 'S'
    start_node['in_node_list'] = True
    start_node['len'] = 0
    open_nodes = [start_node]
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
    if ((result == -1) or (len_to_e < result)) and (len_to_e > -1): result = len_to_e
print (f"Result = {result}")