lines = None
with open('input.txt') as f:
    lines = f.readlines()

stacks = []
for j in range(9):
    stacks.append([])

for i in range(8):
    line = lines[7-i]
    for j in range(9):
        o = line[4*j + 1]
        if o != ' ':
            stacks[j].append(o)

for i in range(10):
    lines.pop(0)

def vis():
    for i in range(9):
        print(i+1, stacks[i])
    print()

def tops():
    result = ""
    for i in range(9):
        result += stacks[i][len(stacks[i])-1]
    print(result)

# part 1
def move(n, x, y):
    print ("move", n, x, y)
    for i in range(n):
        q = stacks[x-1].pop(len(stacks[x-1])-1)
        stacks[y-1].append(q)
        vis()

# part 2
def move2(n, x, y):
    print ("move", n, x, y)
    q = []
    for i in range(n):
        q.insert(0, stacks[x-1].pop(len(stacks[x-1])-1))
    for i in range(n):
        stacks[y-1].append(q.pop(0))
    vis()

vis()
for line in lines:
    n, x, y = line.strip().replace('move ', '').replace(' from ', ',').replace(' to ', ',').split(',')
    move2(int(n), int(x), int(y))

tops()
