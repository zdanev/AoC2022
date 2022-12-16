lines = None
with open('input.txt') as f:
    lines = f.readlines()

line = ''
i = 0

def parse_line(s):
    global line, i
    line = s
    i = 0
    return parse()

def parse():
    if line[i] == '[':
        return parse_list()
    else:
        return parse_int()

def parse_int():
    global i
    x = line[i]
    i += 1
    return int(x)

def parse_list():
    global i
    result = []
    i += 1 # [
    while line[i] != ']':
        x = parse()
        result.append(x)
        if line[i] == ',':
            i += 1

    i += 1 # ]
    return result

def q(a, b):
    if isinstance(a, list) and isinstance(b, list):
        return q_list(a, b)
    elif isinstance(a, list) and not isinstance(b, list):
        return q_list(a, [b])
    elif not isinstance(a, list) and isinstance(b, list):
        return q_list([a], b)
    else:
        return q_int(a, b)

def q_int(a, b):
    if a == b:
        return 0
    elif a < b:
        return 1
    else:
        return -1

def q_list(a, b):
    if len(a) == 0 and len(b) == 0:
        return 0
    elif len(a) == 0:
        return 1
    elif len(b) == 0:
        return -1
    else:
        r = q(a[0], b[0])
        if r == 0:
            return q_list(a[1:], b[1:])
        else:
            return r

# part 1
n = (len(lines) + 1) // 3
result = 0
for index in range(n):
    a = parse_line(lines[3*index])
    b = parse_line(lines[3*index+1])
    if q(a, b) == 1:
        print(index+1)
        result += index+1
print(result)
