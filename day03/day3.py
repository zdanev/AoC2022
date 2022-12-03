lines = None
with open('input.txt') as f:
    lines = f.readlines()

def priority(c):
    if 'a' <= c and c <= 'z':
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27

# part 1
sum = 0
for line in lines:
    line = line.strip()
    n = len(line) // 2
    left = line[:n]
    right = line[n:]

    for c in left:
        if right.find(c) >= 0:
            sum += priority(c)
            break

print(sum)

# part 2
def common(a, b, c):
    for x in a:
        if b.find(x) >= 0 and c.find(x) >= 0:
            return x

sum = 0
for i in range(len(lines) // 3):
    c = common(lines[3*i], lines[3*i+1], lines[3*i+2])
    sum += priority(c)

print(sum)