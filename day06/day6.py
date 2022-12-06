lines = None
with open('input.txt') as f:
    lines = f.readlines()

line = lines[0]

def distinct(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
    return True

# part 1
for i in range(len(line)):
    f = line[i:i+4]
    if distinct(f):
        print(i+4)
        break

# part 2
for i in range(len(line)):
    f = line[i:i+14]
    if distinct(f):
        print(i+14)
        break
