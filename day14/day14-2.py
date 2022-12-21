lines = None
with open('input.txt') as f:
    lines = f.readlines()

q = set()
max = 0
def rock(x, y):
    global max
    q.add((x, y))
    if y > max:
        max = y

def rock1(x, y):
    global max
    q.add((x, y))

def isrock(x, y):
    if y == max + 2: return True
    return (x, y) in q

def wall(x1, y1, x2, y2):
    if x2 < x1: 
        x2, x1 = x1, x2
    if y2 < y1:
        y2, y1 = y1, y2
    if x1 == x2:
        for i in range(y2 - y1+1):
            rock(x1, y1 + i)
    else:
        for i in range(x2 - x1+1):
            rock(x1 + i, y1)

for line in lines:
    pairs = line.strip().split(" -> ")
    for i in range(len(pairs) - 1):
        x1, y1 = pairs[i].split(",")
        x2, y2 = pairs[i + 1].split(",")
        wall(int(x1), int(y1), int(x2), int(y2))

def drop(x, y):
    if isrock(500,0): return False
    while y <= max + 1:
        if isrock(x, y+1) and isrock(x-1, y+1) and isrock(x+1, y+1):
            rock1(x, y)
            return True
        y += 1
        if not (x, y) in q:
            pass
        elif not (x-1, y) in q:
            x -= 1
        else:
            x += 1
    # return False

result = 0
while (drop(500, 0)):
    result += 1
print(result)

