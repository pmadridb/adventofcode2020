with open("./input9.txt", encoding="utf-8") as file:
    numbers = [l.rstrip("\n") for l in file]
numbers = [int(number) for number in numbers]

def part1():
    preamble = 25
    print('invalid number:', get_invalid_number(preamble))

def get_invalid_number(preamble):
    for index in range(preamble, len(numbers)):
        found_pair = False
        for index1 in range(index - preamble, index):
            for index2 in range(index1 + 1, index):
                if (numbers[index1] + numbers[index2]) == numbers[index]:
                    index1 = index
                    index2 = index
                    found_pair = True
        if not found_pair:
            return numbers[index]

def part2():
    preamble = 25
    invalid_number = get_invalid_number(preamble)
    for index in range(len(numbers)):
        sum = 0
        for index1 in range(index, len(numbers)):
            sum += numbers[index1]
            if sum == invalid_number:
                print('encryption weakness:', min(numbers[index:index1+1]) + max(numbers[index:index1+1]))
            elif sum > invalid_number:
                sum = 0
                break
            
part1()
part2()
