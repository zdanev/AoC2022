lines = None
with open('input.txt') as f:
    lines = f.readlines()

dirs = {}
cur = []
for line in lines:
    line = line.rstrip()

    if line == "$ cd ..":
        cur.pop()
        # print (line, cur)
        continue

    if line.startswith("$ cd "):
        cur.append(line[5:])
        # print(line, cur)
        continue

    if line == "$ ls":
        continue

    if line.startswith("dir"):
        continue

    size, fn = line.split(' ')
    dir = ''
    for c in cur:
        dir += '/' + c
        if not dir in dirs:
            dirs[dir] = 0
        dirs[dir] += int(size)

# part 1
sum = 0
for dir in dirs:
    # print(dir, dirs[dir])
    if dirs[dir] < 100000:
        sum += dirs[dir]
print(sum)

# part 2
min = 99999999999
for dir in dirs:
    if 70000000 - dirs["//"] + dirs[dir] > 30000000:
        if dirs[dir] < min:
            min = dirs[dir]
print(min)