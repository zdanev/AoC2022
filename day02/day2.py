lines = None
with open('input.txt') as f:
    lines = f.readlines()

WIN = 6
DRAW = 3
LOSE = 0

ROCK = 1
PAPER = 2 
SCISSORS = 3

def parse(s):
    if s == 'A' or s == 'X': return ROCK
    if s == 'B' or s == 'Y': return PAPER
    if s == 'C' or s == 'Z': return SCISSORS

# part 1
def score(a, b):
    # 1 = rock, 2 = paper, 3, = scisors
    if a == b:
        return DRAW + a
    if a == ROCK:
        if b == PAPER: return WIN + PAPER
        if b == SCISSORS: return LOSE + SCISSORS
    if a == PAPER:
        if b == ROCK: return LOSE + ROCK
        if b == SCISSORS: return WIN + SCISSORS
    if a == SCISSORS:
        if b == ROCK: return WIN + ROCK
        if b == PAPER: return LOSE + PAPER

result = 0
for line in lines:
    pair = line.split(" ")
    result += score(parse(pair[0].strip()), parse(pair[1].strip()))

print(result)

# part 2
def score2(a, b):
    if b == 'X': # lose
        if a == ROCK: return LOSE + SCISSORS
        if a == PAPER: return LOSE + ROCK
        if a == SCISSORS: return LOSE + PAPER
    if b == 'Y': # draw
        if a == ROCK: return DRAW + ROCK
        if a == PAPER: return DRAW + PAPER
        if a == SCISSORS: return DRAW + SCISSORS
    if b == 'Z': # win
        if a == ROCK: return WIN + PAPER
        if a == PAPER: return WIN + SCISSORS
        if a == SCISSORS: return WIN + ROCK 

result = 0
for line in lines:
    pair = line.split(" ")
    result += score2(parse(pair[0].strip()), pair[1].strip())

print(result)
