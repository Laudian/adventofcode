with open("../input.txt") as file:
    data = file.read().split("\n\n")

valid = 0

passports = []

for entry in data:
    passport = {}
    for pair in entry.split():
        field, value = pair.split(":")
        passport[field] = value
    passports.append(passport)
    if len(passport) == 8 or (len(passport) == 7 and "cid" not in passport):
        valid += 1

print("Part 1: " + str(valid))

# Part 2
import functools

def isValid(passport):
    try:
        byr = 1920 <= int(passport["byr"]) <= 2002 and len(passport["byr"]) == 4
        iyr = 2010 <= int(passport["iyr"]) <= 2020 and len(passport["iyr"]) == 4
        eyr = 2020 <= int(passport["eyr"]) <= 2030 and len(passport["eyr"]) == 4
        unit = passport["hgt"][-2:]
        size = int(passport["hgt"][:-2])
        hgt = (unit == "cm" and (150 <= size <= 193)) or (unit == "in" and (59 <= size <= 76))
        color = passport["hcl"][1:].lower()
        hcl = passport["hcl"][0] == "#" and len(color) == 6 and functools.reduce(lambda start, x : start + (x in "0123456789abcdef"), color, 0) == 6
        ecl = passport["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
        nr = passport["pid"]
        pid = len(nr) == 9 and functools.reduce(lambda start, x : start + (x in "0123456789"), nr, 0) == 9
        return byr and iyr and eyr and hgt and hcl and ecl and pid
    except:
        return False

counter = 0
for passport in passports:
    counter += isValid(passport)

print("Part 2: " + str(counter))