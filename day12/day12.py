lines = None
with open('input.txt') as f:
    lines = f.readlines()

# part 1
# start = "S"
# end = "E"

# part 2
start = 'E'
end = 'a'

rows = len(lines)
cols = len(lines[0].strip())
x0 = y0 = 0
try:
    for r in range(rows):
        for c in range(cols):
            if lines[r][c] == start:
                x0 = c
                y0 = r
                raise StopIteration
except:
    pass

def go(x, y, h, d):
    if x < 0 or y < 0 or x > cols - 1 or y > rows - 1: return
    if (x, y) in v: return
    if start == "S" and ord(lines[y][x]) > h+1: return
    if start == "E" and ord(lines[y][x]) < h-1: return
    if lines[y][x] == end: 
        print(d)
        exit()
    q.append((x, y, d))
    v.add((x, y))

v = set()
q = [(x0, y0, 0)]
v.add((x0, y0))
while len(q) > 0:
    p = q.pop(0)
    x = p[0]
    y = p[1]
    d = p[2] + 1
    h = ord(lines[y][x])  
    if lines[y][x] == "S": h = ord('a') # part 1
    if lines[y][x] == "E": h = ord('z') # part 2

    go(x-1, y, h, d)
    go(x+1, y, h, d)
    go(x, y-1, h, d)
    go(x, y+1, h, d)
