import re
import regex

with open("./input7.txt", encoding="utf-8") as file:
    rules = [l.rstrip("\n") for l in file]

def part1():
    nodes = {}
    for rule in rules:
        name, children = parse_rule(rule)
        nodes[name] = children[1]
    bags = set()
    bags_can_contain(nodes, 'shiny gold ', bags)
    print(len(bags))

def part2():
    nodes = {}
    for rule in rules:
        parse_rule_part2(rule, nodes)
    amount = count_bags(nodes, 'shiny gold ')
    print(amount)

def count_bags(nodes, color):
    amount = 0
    for node in nodes[color]:
        amount += (nodes[color][node] + (nodes[color][node] * count_bags(nodes, node)))
    return amount

def bags_can_contain_with_amount(nodes, bag, bags):
    for node in nodes:
        for child in nodes[node][1]:
            if child == bag:
                if node in bags:
                    bags[node] += nodes[node][0]
                else:
                    bags[node] = nodes[node][0]
                bags_can_contain_with_amount(nodes, node, bags)

def bags_can_contain(nodes, bag, bags):
    for node in nodes:
        for child in nodes[node]:
            if child == bag:
                bags.add(node)
                bags_can_contain(nodes, node, bags)

def parse_rule_part2(rule, rules_dict):
    rules = rule.split(',')
    reg = re.compile('(?P<data>(\w*\s){2})bags contain\s(((?P<amount>[0-9])\s(?P<child>(\w*\s){2})(bag|bags))|(no\sother\sbags\.))')
    match = reg.search(rules[0].strip())
    bag = match.group('data')
    rules_dict[bag] = {}
    if match.group('child') is not None:
        rules_dict[bag][match.group('child')] = int(match.group('amount'))
    reg = re.compile('(?P<amount>[0-9])\s(?P<child>(\w*\s){2})(bag|bags)')
    for i in range(1,len(rules)):
        match = reg.search(rules[i].strip())
        rules_dict[bag][match.group('child')] = int(match.group('amount'))

def parse_rule(rule):
    re = regex.compile('(?P<data>(\w*\s){2})bags contain\s(((?P<amount>[0-9])\s(?P<child>(\w*\s){2})(bag|bags)((\.\s|,\s)|\.))*)|(no\sother\sbags\.)')
    match = re.match(rule)
    return match.group('data'), [[int(i) for i in match.captures('amount')], set(match.captures('child'))]

part1()
part2()
