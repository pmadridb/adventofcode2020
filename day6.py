import re
with open("./input6.txt", encoding="utf-8") as file:
    answers_list = [l.rstrip("\n") for l in file]

def part1():
    unique_answers = 0
    answers = ''
    for line in answers_list:
        if not line:
            unique_answers+= len(list(dict.fromkeys(answers)))
            answers = ''
        else:
            answers = answers + line
    unique_answers+= len(list(dict.fromkeys(answers)))
    print(unique_answers)

part1()
