with open("./input5.txt", encoding="utf-8") as file:
    passes = [l.rstrip("\n") for l in file]

def part1():
    highest_seat_id = 0
    for bpass in passes:
        row = get_row(bpass[:7], range(128))
        seat = get_row(bpass[7:11], range(8))
        seat_id = (row * 8) + seat
        if highest_seat_id < seat_id:
            highest_seat_id = seat_id
    print('Highest seat ID', highest_seat_id)

def get_row(bpass, row_range):
    if bpass[0] == 'F' or bpass[0] == 'L':
        if len(bpass) == 1:
            return row_range.start
        else:
            return get_row(bpass[1:len(bpass)], range(row_range.start, row_range.stop - int((row_range.stop - row_range.start)/2)))
    else:
        if len(bpass) == 1:
            return row_range.stop -1
        else:
            return get_row(bpass[1:len(bpass)], range(row_range.start + int((row_range.stop - row_range.start)/2), row_range.stop))

def part2():
    seat_ids = []
    for bpass in passes:
        row = get_row(bpass[:7], range(128))
        seat = get_row(bpass[7:11], range(8))
        seat_ids.append((row * 8) + seat)
    seat_ids.sort()
    for index in range(len(seat_ids) - 1):
        if (seat_ids[index - 1] + 2) == seat_ids[index]:
            print('My seat ID:', seat_ids[index] - 1)
            break


part1()
part2()