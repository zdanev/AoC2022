lines = None
with open('input.txt') as f:
    lines = f.readlines()

# part 1
# n = 2

# part 2
n = 10

rope = []
for i in range(n):
    rope.append((0, 0))

def move_head(dir):
    head = rope[0]
    if dir == "U": 
        head = (head[0], head[1] - 1)
    if dir == "D": 
        head = (head[0], head[1] + 1)
    if dir == "L": 
        head = (head[0] - 1, head[1])
    if dir == "R": 
        head = (head[0] + 1, head[1])
    rope[0] = head

def move_tail(i):
    prev = rope[i-1]
    cur = rope[i]

    if cur[0] == prev[0] - 2 and cur[1] == prev[1] - 2:
        cur = (prev[0] - 1, prev[1] - 1)
    if cur[0] == prev[0] + 2 and cur[1] == prev[1] + 2:
        cur = (prev[0] + 1, prev[1] + 1)
    if cur[0] == prev[0] - 2 and cur[1] == prev[1] + 2:
        cur = (prev[0] - 1, prev[1] + 1)
    if cur[0] == prev[0] + 2 and cur[1] == prev[1] - 2:
        cur = (prev[0] + 1, prev[1] - 1)

    if cur[0] == prev[0] - 2:
        cur = (prev[0] - 1, prev[1])
    if cur[0] == prev[0] + 2:
        cur = (prev[0] + 1, prev[1])
    if cur[1] == prev[1] - 2:
        cur = (prev[0], prev[1] - 1)
    if cur[1] == prev[1] + 2:
        cur = (prev[0], prev[1] + 1)

    rope[i] = cur

q = set()
for line in lines:
    dir, steps = line.split(" ")
    steps = int(steps)

    for step in range(steps):
        move_head(dir)
        for i in range(n-1):
            move_tail(i+1)

        tail = rope[n-1]
        q.add(tail)

print(len(q))
