import re
with open("./input14.txt", encoding="utf-8") as file:
    input = [l.rstrip("\n") for l in file]

def part1():
    memory = {}
    mask = ''
    for entry in input:
        allocation = entry.split('=')
        if allocation[0] == 'mask ':
            mask = allocation[1].strip()
        else:
            reg = re.compile('\[(?P<data>[0-9]*)\]')
            match = reg.search(allocation[0].strip())
            mem_position = match.group('data')
            memory[mem_position] = apply_mask(mask, f'{int(allocation[1].strip()):b}'.zfill(len(mask)))
    print(sum([int(num, 2) for num in memory.values()]))

def apply_mask(mask, value):
    value_list = list(value)
    for idx, c in enumerate(mask):
        if c != 'X':
            value_list[idx] = c
    return ''.join(value_list)

def apply_mask_part2(mask, value):
    value_list = list(value)
    for idx, c in enumerate(mask):
        if c == 'X' or c == '1':
            value_list[idx] = c
    return ''.join(value_list)

def get_floating(masked):
    values = []
    x_found = False
    for value in masked:
        value_list = list(value)
        for idx, c in enumerate(value):
            if c == 'X':
                value_list[idx] = '0'
                values.append(''.join(value_list))
                value_list[idx] = '1'
                values.append(''.join(value_list))
                x_found = True
                break
    if not x_found:
        return masked
    return get_floating(values)

def part2():
    mask = ''
    memory = {}
    for entry in input:
        allocation = entry.split('=')
        if allocation[0] == 'mask ':
            mask = allocation[1].strip()
        else:
            reg = re.compile('\[(?P<data>[0-9]*)\]')
            match = reg.search(allocation[0].strip())
            mem_position = match.group('data')
            masked = apply_mask_part2(mask, f'{int(mem_position):b}'.zfill(len(mask)))
            for position in get_floating([masked]):
                memory[position] = allocation[1].strip()
    print(sum([int(num) for num in memory.values()]))

part1()
part2()

