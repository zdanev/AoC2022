lines = None
with open('input.txt') as f:
    lines = f.readlines()

q = [20, 60, 100, 140, 180, 220]
result = 0

x = 1
cycle = 0
def ping():
    global cycle, result
    
    # part 2
    pixel = cycle % 40
    if pixel - 1 <= x and x <= pixel + 1:
        print("#", end="")
    else:
        print(".", end="")
    if pixel == 39:
        print("")
    #.

    cycle += 1
    if cycle in q:
        result += cycle * x

for line in lines:
    line = line.strip()
    if line == "noop":
        ping()
        continue
    _, i = line.split(' ')
    i = int(i)

    ping()
    ping()
    x += i

print(result)
