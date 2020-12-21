with open("./input12.txt", encoding="utf-8") as file:
    directions = [l.rstrip("\n") for l in file]

def part1():
    current_direction = 'E'
    x_axis, y_axis = 0, 0
    for direction in directions:
        action = direction[:1]
        if action == 'E' or action == 'W' or action == 'N' or action == 'S':
            x_axis, y_axis = move_in_direction(action, int(direction[1:]), x_axis, y_axis)
        elif action == 'F':
            x_axis, y_axis = move_in_direction(current_direction, int(direction[1:]), x_axis, y_axis)
        elif action == 'L' or action == 'R':
            current_direction = turn_direction(action, int(direction[1:]), current_direction)
    print(abs(x_axis) + abs(y_axis))            

def part2():
    ship_x_axis, ship_y_axis = 0, 0
    waypoint_x_axis, waypoint_y_axis = 10, 1
    for direction in directions:
        action = direction[:1]
        if action == 'E' or action == 'W' or action == 'N' or action == 'S':
            waypoint_x_axis, waypoint_y_axis = move_in_direction(action, int(direction[1:]), waypoint_x_axis, waypoint_y_axis)
        elif action == 'F':
            ship_x_axis += (waypoint_x_axis * int(direction[1:]))
            ship_y_axis += (waypoint_y_axis * int(direction[1:]))
        elif action == 'L' or action == 'R':
            waypoint_x_axis, waypoint_y_axis = rotate_waypoint(action, int(direction[1:]), waypoint_x_axis, waypoint_y_axis)
    print(abs(ship_x_axis) + abs(ship_y_axis))            

def rotate_waypoint(action, degrees, waypoint_x_axis, waypoint_y_axis):
    new_x_axis, new_y_axis = 0, 0
    new_direction = degrees / 90
    if action == 'L':
        if new_direction == 1:
            new_x_axis = -waypoint_y_axis
            new_y_axis = waypoint_x_axis
        elif new_direction == 2:
            new_x_axis = -waypoint_x_axis
            new_y_axis = -waypoint_y_axis
        else:
            new_x_axis = waypoint_y_axis
            new_y_axis = -waypoint_x_axis
    else:
        if new_direction == 1:
            new_x_axis = waypoint_y_axis
            new_y_axis = -waypoint_x_axis
        elif new_direction == 2:
            new_x_axis = -waypoint_x_axis
            new_y_axis = -waypoint_y_axis
        else:
            new_x_axis = -waypoint_y_axis
            new_y_axis = waypoint_x_axis
    return new_x_axis, new_y_axis

def move_in_direction(action, value, x_axis, y_axis):
    if action == 'E':
        x_axis += value
    elif action == 'W':
        x_axis -= value
    elif action == 'N':
        y_axis += value
    elif action == 'S':
        y_axis -= value
    return x_axis, y_axis

def turn_direction(action, degrees, current_direction):
    directions = ['N', 'E', 'S', 'W']
    current_index = directions.index(current_direction)
    new_direction = degrees / 90
    while new_direction != 0:
        if action == 'R':
            if current_index + 1 > 3:
                current_index = 0
            else:
                current_index += 1
        elif action == 'L':
            if current_index - 1 < 0:
                current_index = 3
            else:
                current_index -= 1
        new_direction -= 1
    return directions[current_index]

part1()
part2()