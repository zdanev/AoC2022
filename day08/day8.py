lines = None
with open('input.txt') as f:
    lines = f.readlines()

rows = len(lines)
cols = len(lines[0].strip())

q = []
qq = []
for row in range(rows):
    q.append([])
    qq.append([])
    for col in range(cols):
        q[row].append(int(lines[row][col]))
        qq[row].append(0)

# part 1

# L -> R
for row in range(rows):
    h = -1
    for col in range(cols):
        if q[row][col] > h:
            qq[row][col] = 1
            h = q[row][col]

# R -> L
for row in range(rows):
    h = -1
    for c in range(cols):
        col = cols - c - 1
        if q[row][col] > h:
            qq[row][col] = 1
            h = q[row][col]

# T -> B
for col in range(cols):
    h = -1
    for row in range(rows):
        if q[row][col] > h:
            qq[row][col] = 1
            h = q[row][col]

# B -> T
for col in range(cols):
    h = -1
    for r in range(rows):
        row = rows - r - 1
        if q[row][col] > h:
            qq[row][col] = 1
            h = q[row][col]

# for row in range(rows):
#     for col in range(cols):
#         print(qq[row][col], end='')
#     print('')

count = 0
for row in range(rows):
    for col in range(cols):
        count += qq[row][col]
print(count)

# part 2

def score(r, c):
    # if r == 0 or c == 0 or r == rows-1 or c == cols -1: return 0
    h = q[r][c]
    s1 = s2 = s3 = s4 = 0

    # L
    cc = c
    while cc > 0:
        s1 += 1
        cc -= 1
        if q[r][cc] >= h: break

    # R
    cc = c
    while cc < cols-1:
        s2 += 1
        cc += 1
        if q[r][cc] >= h: break

    # U
    rr = r
    while rr > 0:
        s3 += 1
        rr -= 1
        if q[rr][c] >= h: break

    # D
    rr = r
    while rr < rows-1:
        s4 += 1
        rr += 1
        if q[rr][c] >= h: break
    
    return s1 * s2 * s3 * s4

max = 0
for r in range(rows):
    for c in range(cols):
        s = score(r, c)
        if s > max:
            max = s
print(max)