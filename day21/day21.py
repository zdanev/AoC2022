lines = None
with open("input.txt") as f:
    lines = f.readlines()

q = {}
for line in lines:
    name, expr = line.strip().split(": ")
    q[name] = expr

def eval(name):
    expr = q[name]
    if expr.isnumeric():
        return int(expr)
    else:
        name1, op, name2 = expr.split(" ")
        val1 = eval(name1)
        val2 = eval(name2)
        if op == "+": return val1 + val2 
        elif op == "-": return val1 - val2
        elif op == "*": return val1 * val2
        elif op == "/": return val1 // val2

print(eval("root"))