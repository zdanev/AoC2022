lines = None
with open('input.txt') as f:
    lines = f.readlines()

# a c d b
# c a b d
def contains(a, b, c, d):
    return (a <= c and d <= b) or (c <= a and b <= d)

def overlaps(a, b, c, d):
    return (a <= c and c <= b) or (a <= d and d <= b) or (c <= a and a <= d) or (c <= b and b <= d)

count1 = 0
count2 = 0
for line in lines:
    line = line.strip().replace(',', '-')
    a, b, c, d = map(int, line.split('-'))

    if contains(a, b, c, d): count1 += 1
    if overlaps(a, b, c, d): count2 += 1

print(count1)
print(count2)