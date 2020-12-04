with open("c:/Users/pmadrid/Downloads/adventofcode/input2.txt", encoding="utf-8") as file:
    lines = [l.rstrip("\n") for l in file]

def parseLine(line):
    split = line.split(":")
    policy = split[0]
    policySplit = policy.split(" ")
    times = policySplit[0]
    timesSplit = times.split("-")
    return (int(timesSplit[0]), int(timesSplit[1]), policySplit[1], split[1].strip())

tuples = [parseLine(line) for line in lines]

def isPasswordValid1(tuple):
    count = tuple[3].count(tuple[2])
    return count >= tuple[0] and count <= tuple[1]

def isPasswordValid2(tuple):
    return (tuple[3][tuple[0]-1] == tuple[2]) ^ (tuple[3][tuple[1]-1] == tuple[2])

validPasswords1 = 0
validPasswords2 = 0
for tuple in tuples:
    if isPasswordValid1(tuple):
        validPasswords1 += 1
    if isPasswordValid2(tuple):
        validPasswords2 += 1

print("Valid passwords policy 1:", validPasswords1)
print("Valid passwords policy 2:", validPasswords2)