lines = None
with open('input.txt') as f:
    lines = f.readlines()

# part 1
max = 0
current = 0
sums = []
for line in lines:
    if line == "\n":
        if current > max:
            max = current
        sums.append(current)
        current = 0
    else:
        current += int(line)

if current > max:
    max = current
sums.append(current)

print(max)

# part 2
sums.sort(reverse=True)
print(sums[0] + sums[1] + sums[2])