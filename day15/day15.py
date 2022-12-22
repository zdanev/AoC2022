lines = None
with open("input.txt") as f:
    lines = f.readlines()
y = 2000000

def dist(x0, y0, x1, y1):
    return abs(x0 - x1) + abs(y0 - y1)

ranges = []
def add(sx, sy, bx, by):
    d = dist(sx, sy, bx, by)
    q = abs(y - sy)
    if q <= d:
        dq = d - q
        ranges.append((sx - dq, sx + dq)) 

for line in lines:
    line = line.replace("Sensor at x=", "") \
        .replace(" y=", "") \
        .replace(": closest beacon is at x=", ",")
    sx, sy, bx, by = map(int, line.split(","))
    add(sx, sy, bx, by)

def overlap(ri, rj):
    if ri[0] <= rj[0] and rj[0] <= ri[1]: return True
    if ri[0] <= rj[1] and rj[1] <= ri[1]: return True
    if rj[0] <= ri[0] and ri[0] <= rj[1]: return True
    if rj[0] <= ri[1] and ri[1] <= rj[1]: return True
    return False

flag = True
while (flag):
    flag = False
    try:
        for i in range(len(ranges) - 1):
            for j in range(i + 1, len(ranges)):
                ri = ranges[i]
                rj = ranges[j]
                if overlap(ri, rj):
                    rn = (min(ri[0], rj[0]), max(ri[1], rj[1]))
                    ranges.remove(ri)
                    ranges.remove(rj)
                    ranges.append(rn)
                    raise Exception("break x2")
    except:
        flag = True

count = 0
for (a, b) in ranges:
    count += b - a
print(count)
