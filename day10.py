with open("./input10.txt", encoding="utf-8") as file:
    jolts = [l.rstrip("\n") for l in file]
jolts = [int(number) for number in jolts]

def part1():
    jolts.append(0)
    jolts.append(max(jolts)+3)
    jolts.sort()
    print(find_adapters(0, 0, 0))

def find_adapters(effective_joltage, one_diffs, three_diffs):
    for index in range(len(jolts)):
        if (effective_joltage + 1) == jolts[index]:
            effective_joltage = jolts[index]
            one_diffs += 1
        elif (effective_joltage + 3) == jolts[index]:
            effective_joltage = jolts[index]
            three_diffs += 1
    return one_diffs * three_diffs
    
def part2():
    pathCounts = [0] * len(jolts)
    pathCounts[0] = 1
    for i in range(1, len(jolts)):
        for j in range(1, 4):
            indexToCheck = i - j
            if indexToCheck < 0 or (jolts[indexToCheck] < jolts[i] - 3):
                continue
            pathCounts[i] += pathCounts[indexToCheck]
    print("Number of arrangements:", pathCounts[len(pathCounts) - 1])
    
part1()
part2()