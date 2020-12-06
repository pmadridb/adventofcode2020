import re
with open("./input4.txt", encoding="utf-8") as file:
    passports = [l.rstrip("\n") for l in file]

fields_regex = {'byr':'19[2-9][0-9]|200[0-2]', 
                'iyr':'201[0-9]|2020', 
                'eyr':'202[0-9]|2030', 
                'hgt':'(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6]|19[0-3])in', 
                'hcl':'#[a-z0-9]{6}', 
                'ecl':'amb|blu|brn|gry|grn|hzl|oth', 
                'pid':'[0-9]{9}',
                'cid':'.*'}

def parse_passport(passport):
    valid_passport = {'byr':False, 'iyr':False, 'eyr':False, 'hgt':False, 'hcl':False, 'ecl':False, 'pid':False}
    parts = passport.split()
    for token in parts:
        entry = token.split(':')
        valid_passport[entry[0]] = re.search(fields_regex[entry[0]], entry[1]) != None
    if False in list(valid_passport.values()):
        return 0
    else:
        return 1

valid_passports = 0
passport = ''
for line in passports:
    if not line:
        valid_passports+= parse_passport(passport.strip())
        passport = ''
    else:
        passport = passport + ' ' + line

valid_passports+= parse_passport(passport.strip())
print(valid_passports)
