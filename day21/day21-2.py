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

def contains_humn(name):
    if name == "humn": return True
    expr = q[name]
    if expr.isnumeric():
        return False
    else:
        name1, op, name2 = expr.split(" ")
        return contains_humn(name1) or contains_humn(name2)

def eval_part2(name, target):
    if name == "humn":
        print(target)
        return target
    
    expr = q[name]
    if expr.isnumeric():
        return int(expr)
    else:
        name1, op, name2 = expr.split(" ")
        if contains_humn(name1):
            expr = name1
            result = eval(name2)

            if name == "root":    
                return eval_part2(expr, result)
            if op == "+":
                return eval_part2(expr, target - result)
            elif op == "-":
                return eval_part2(expr, target + result)
            elif op == "*":
                return eval_part2(expr, target // result)
            elif op == "/":
                return eval_part2(expr, target * result)
        else:
            expr = name2
            result = eval(name1)

            if name == "root":    
                return eval_part2(expr, result)
            if op == "+":
                return eval_part2(expr, target - result)
            elif op == "-":
                return eval_part2(expr, result - target)
            elif op == "*":
                return eval_part2(expr, target // result)
            elif op == "/":
                return eval_part2(expr, result // target)

# part 1
# print(eval("root"))

# part 2
eval_part2("root", 0)