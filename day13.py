from math import gcd
with open("./input13.txt", encoding="utf-8") as file:
    input = [l.rstrip("\n") for l in file]

def part1():
    estimate = int(input[0])
    routes = input[1].split(',')
    departure_times = {}
    for route in routes:
        if route == 'x': continue
        time = 0
        while time < estimate:
            time += int(route)
        departure_times[int(route)] = time - estimate
    minimun = min(departure_times, key=departure_times.get)
    print(minimun * departure_times[minimun])

def part2():
    buses = input[1].split(',')
    mods = {}
    for idx, bus in enumerate(buses):
        if bus != 'x':
            mods[int(bus)] = -idx % int(bus)

    iterator = 0
    increment = 1
    for bus in mods.keys():
        while iterator % int(bus) != mods[int(bus)]:
            iterator += increment
        increment *= int(bus)

    print(iterator)

part1()
part2()
