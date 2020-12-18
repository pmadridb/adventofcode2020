
import copy
with open("./input11.txt", encoding="utf-8") as file:
    seats = [l.rstrip("\n") for l in file]
seats = [list(row) for row in seats]
def part1():
    global seats
    while True:
        changed = False
        new_seats = copy.deepcopy(seats)
        for row in range(len(seats)):
            for index in range(len(seats[row])):
                current_seat = seats[row][index]
                if current_seat == '.': continue
                elif current_seat == 'L' and count_adjacent_seats(row, index, '#') == 0:
                    new_seats[row][index] = '#'
                    changed = True
                elif current_seat == '#' and count_adjacent_seats(row, index, '#') >= 4:
                    new_seats[row][index] = 'L'
                    changed = True
        if changed == False: break
        seats = copy.deepcopy(new_seats)
    occupied_seats = 0
    for row in seats:
        occupied_seats += row.count('#')
    print('Occupied seats:', occupied_seats)

def count_adjacent_seats(row, index, character):
    count = 0
    if row != 0:
        count += count_adjacent_seats_in_row(row - 1, index, character)
    if index != 0 and seats[row][index - 1] == character:
        count += 1
    if index < len(seats[0])-1 and seats[row][index + 1] == character:
        count += 1
    if row < len(seats) - 1:
        count += count_adjacent_seats_in_row(row + 1, index, character)
    return count
def count_adjacent_seats_in_row(row, index, character):
    count = 0
    if index != 0 and seats[row][index - 1] == character:
        count += 1
    if seats[row][index] == character:
        count += 1
    if index < len(seats[0])-1 and seats[row][index + 1] == character:
        count += 1
    return count

def part2():
    with open("./input11.txt", encoding="utf-8") as file:
        seats = [l.rstrip("\n") for l in file]
    seats = [list(row) for row in seats]

    new_seats = copy.deepcopy(seats)
    while True:
        changed = False
        for row in range(len(seats)):
            for index in range(len(seats[row])):
                current_seat = seats[row][index]
                if current_seat == '.': continue
                elif current_seat == 'L' and count_seats(row, index, seats) == 0:
                    new_seats[row][index] = '#'
                    changed = True
                elif current_seat == '#' and count_seats(row, index, seats) >= 5:
                    new_seats[row][index] = 'L'
                    changed = True
        if changed == False: break
        seats = copy.deepcopy(new_seats)
    occupied_seats = 0
    for row in new_seats:
        occupied_seats += row.count('#')
    print('Occupied seats:', occupied_seats)

def count_seats(row, index, seats):
    count = 0
    index_x = row - 1
    index_y_left = index - 1
    index_y_right = index + 1
    nw, n, ne = -1, -1, -1
    while index_x >= 0 and ((nw + n + ne) < 3):
        if index_y_left >= 0 and nw == -1:
            if seats[index_x][index_y_left] == '#':
                nw = 1
            elif seats[index_x][index_y_left] == 'L':
                nw = 0
        if n == -1:
            if seats[index_x][index] == '#':
                n = 1
            elif seats[index_x][index] == 'L':
                n = 0
        if index_y_right < len(seats[0]) and ne == -1:
            if seats[index_x][index_y_right] == '#':
                ne = 1
            elif seats[index_x][index_y_right] == 'L':
                ne = 0
        index_y_left -= 1
        index_y_right += 1
        index_x -= 1
    if nw > 0: count += nw
    if n > 0: count += n
    if ne > 0: count += ne
    index_x = row + 1
    index_y_left = index - 1
    index_y_right = index + 1
    sw, s, se = -1, -1, -1
    while index_x < len(seats) and ((sw + s + se) < 3):
        if index_y_left >= 0 and sw == -1:
            if seats[index_x][index_y_left] == '#':
                sw = 1
            elif seats[index_x][index_y_left] == 'L':
                sw = 0
        if s == -1:
            if seats[index_x][index] == '#':
                s = 1
            elif seats[index_x][index] == 'L':
                s = 0
        if index_y_right < len(seats[0]) and se == -1:
            if seats[index_x][index_y_right] == '#':
                se = 1
            elif seats[index_x][index_y_right] == 'L':
                se = 0
        index_y_left -= 1
        index_y_right += 1
        index_x += 1
    if sw > 0: count += sw
    if s > 0: count += s
    if se > 0: count += se
    for i in range(index - 1, -1, -1):
        if seats[row][i] == '#':
            count += 1
            break
        elif seats[row][i] == 'L':
            break
    for i in range(index + 1, len(seats[row])):
        if seats[row][i] == '#':
            count += 1
            break
        elif seats[row][i] == 'L':
            break
    return count

part1()
part2()