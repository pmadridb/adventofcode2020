with open("./input3.txt", encoding="utf-8") as file:
    forest = file.read().replace('\n', '')

tree = "#"
length = 31

def find_tress(slope_x, slope_y):
    index = 0
    number_of_trees = 0
    cursor = 0
    while cursor < len(forest):
        if forest[cursor] == tree:
            number_of_trees += 1
        index += 1
        cursor = ((slope_x * index) % length + (slope_y * length * index))
    return number_of_trees

# Part 1:
print(find_tress(3, 1))

# Part 2
print(find_tress(1, 1) * find_tress(3, 1) * find_tress(5, 1) * find_tress(7, 1) * find_tress(1, 2))