lines = None
with open('test.txt') as f:
    lines = f.readlines()

n = len(lines) // 7

item = []
operator = []
value = []
test = []
if_true = []
if_false = []
count= []

for i in range(len(lines)):
    line = lines[i].strip()
    if i % 7 == 1:
        items = list(map(int, line.replace("Starting items: ", "").split(", ")))
        item.append(items)
    if i % 7 == 2:
        op, val = line.replace("Operation: new = old ", "").split(" ")
        operator.append(op)
        value.append(val)
    if i % 7 == 3:
        div = line.replace("Test: divisible by ", "")
        test.append(int(div))
    if i % 7 == 4:
        m = line.replace("If true: throw to monkey ", "")
        if_true.append(int(m))
    if i % 7 == 5:
        m = line.replace("If false: throw to monkey ", "")
        if_false.append(int(m))

for monkey in range(n):
    count.append(0)

for round in range(20):
    if round % 10 == 0: print(round)
    for monkey in range(n):
        for i in item[monkey]:
            count[monkey] += 1
            v = i
            if operator[monkey] == "*":
                if value[monkey] == "old":
                    v *= v
                else:
                    v *= int(value[monkey])
            elif operator[monkey] == '+':
                v += int(value[monkey])
            v //= 3
            if v % test[monkey] == 0:
                throw_to = if_true[monkey]
            else:
                throw_to = if_false[monkey]
            item[throw_to].append(v)
        item[monkey] = []

count.sort(reverse=True)
print(count[0]*count[1])
