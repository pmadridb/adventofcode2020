with open("./input.txt", encoding="utf-8") as file:
    numbers = [l.rstrip("\n") for l in file]

numbers = [int(number) for number in numbers]

def part1():
    for lineA in numbers:
        for lineB in numbers:
            for lineC in numbers:
                if int(lineA) + int(lineB) + int(lineC) == 2020:
                    print(int(lineA) * int(lineB) * int(lineC))

def part2():
    for i in range(0, len(numbers)):
        for j in range(i, len(numbers)):
            for k in range(j, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == 2020:
                    print(f'{numbers[i]} * {numbers[j]} * {numbers[k]} == {numbers[i]*numbers[j]*numbers[k]}')

part1()
part2()