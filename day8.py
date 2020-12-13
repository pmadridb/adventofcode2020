import re

with open("./input8.txt", encoding="utf-8") as file:
    instructions = [l.rstrip("\n") for l in file]

def part1():
    accumulator = 0
    instructions_history = [0]
    cursor = 0
    instruction = instructions[0].split(' ')
    execute_instruction_part1(instruction[0], int(instruction[1]), cursor, accumulator, instructions_history)

def execute_instruction_part1(operation, value, cursor, accumulator, instructions_history):
    instructions_history.append(cursor)
    if operation == 'nop':
        cursor += 1
    elif operation == 'acc':
        cursor += 1
        accumulator += value
    else:
        cursor += value
    if cursor not in instructions_history:
        instruction = instructions[cursor].split(' ')
        execute_instruction_part1(instruction[0], int(instruction[1]), cursor, accumulator, instructions_history)
    else:
        print(accumulator)

def execute_instruction_part2(operation, value, cursor, accumulator, instructions_history, instructions_changed, instruction_changed_performed):
    instructions_history.append(cursor)
    if operation == 'nop':
        if instruction_changed_performed or cursor in instructions_changed:
            cursor += 1
        else:
            instruction_changed_performed = True
            instructions_changed.append(cursor)
            cursor += value
    elif operation == 'acc':
        cursor += 1
        accumulator += value
    else:
        if instruction_changed_performed or cursor in instructions_changed:
            cursor += value
        else:
            instruction_changed_performed = True
            instructions_changed.append(cursor)
            cursor += 1
    if cursor == len(instructions):
        print(accumulator)
        return True
    elif cursor not in instructions_history:
        instruction = instructions[cursor].split()
        return execute_instruction_part2(instruction[0], int(instruction[1]), cursor, accumulator, instructions_history, instructions_changed, instruction_changed_performed)
    else:
        return False

def part2():
    instructions_changed = []
    result_found = False
    while not result_found:
        accumulator = 0
        instructions_history = []
        cursor = 0
        instruction_changed_performed = False
        instruction = instructions[0].split()
        result_found = execute_instruction_part2(instruction[0], int(instruction[1]), cursor, accumulator, instructions_history, instructions_changed, instruction_changed_performed)

part1()
part2()