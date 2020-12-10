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

def part2():
    unique_answers = 0
    answers = []
    for line in answers_list:
        if not line:
            unique_answers+= dupe_answers(answers)
            answers = []
        else:
            answers.append(line)
    unique_answers+= dupe_answers(answers)
    print(unique_answers)

def dupe_answers(answers):
    seen = {}
    for answer in answers:
        for char in answer:
            if char not in seen:
                seen[char] = 1
            else:
                seen[char] += 1
    return list(seen.values()).count(len(answers))

part1()
part2()