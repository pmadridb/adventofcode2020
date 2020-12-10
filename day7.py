import regex

with open("./input7.txt", encoding="utf-8") as file:
    rules = [l.rstrip("\n") for l in file]

def part1():
    nodes = {}
    for rule in rules:
        name, children = parse_rule(rule)
        if name in nodes:
            nodes[name].extend(children)
        else:
            nodes[name] = children
    bags = set()
    bags_can_contain(nodes, 'shiny gold ', bags)
    print(len(bags))

def bags_can_contain(nodes, bag, bags):
    for node in nodes:
        for child in nodes[node]:
            if child == bag:
                bags.add(node)
                bags_can_contain(nodes, node, bags)

def parse_rule(rule):
    re = regex.compile('(?P<data>(\w*\s){2})bags contain\s(([0-9]\s(?P<child>(\w*\s){2})(bag|bags)((\.\s|,\s)|\.))*)|(no\sother\sbags\.)')
    match = re.match(rule)
    return match.group('data'), set(match.captures('child'))

part1()

