def read_file(f):
    with open(f) as f:
        content = [line.strip().split(" ") for line in f.readlines()]
    return content

def read_comma_list(f):
    with open(f) as f:
        content = f.readline()
    return [int(x) for x in content.split(",")]