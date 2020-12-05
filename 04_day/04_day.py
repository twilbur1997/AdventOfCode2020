"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)

byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.

"""
# Passports are separated by blank lines.

num_len = 4 # num of digits in byr, iyr, eyr

min_byr = 1920
max_byr = 2002

min_iyr = 2010
max_iyr = 2020

min_eyr = 2020
max_eyr = 2030

min_hgt_in = 59
max_hgt_in = 76

min_hgt_cm = 150
max_hgt_cm = 193

hcl_char_set = {"a", "b", "c", "d", "e", "f"}

ecl_set = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def check_byr(byr):
    if (len(byr) != num_len):
        # print("byr length error: ", byr, " ",len(byr))
        return False
    return (int(byr)>=min_byr and int(byr)<=max_byr)

def check_iyr(iyr):
    if (len(iyr) != num_len):
        return False
    return (int(iyr)>=min_iyr and int(iyr)<=max_iyr)

def check_eyr(eyr):
    if (len(eyr) != num_len):
        return False
    return (int(eyr)>=min_eyr and int(eyr)<=max_eyr)


def check_hgt(hgt):
    if hgt[-2:] == "cm":
        return check_hgt_cm(hgt[:-2])
    elif hgt[-2:] == "in":
        return check_hgt_in(hgt[:-2])
    return False

def check_hgt_in(hgt):
    return (int(hgt)>=min_hgt_in and int(hgt)<=max_hgt_in)

def check_hgt_cm(hgt):
    return (int(hgt)>=min_hgt_cm and int(hgt)<=max_hgt_cm)


def check_hcl(hcl):
    # print("\n\n", hcl)
    hcl = hcl.strip()
    if len(hcl) != 7:
        # print("hcl invalid length: ", len(hcl))
        return False
    if hcl[0] != "#":
        # print("'#' missing")
        return False
    hcl = hcl[1:]
    for char in hcl:
        if not char.isdigit() and char not in hcl_char_set:
            # print("invalid character")
            return False
    return True

def check_ecl(ecl):
    if ecl not in ecl_set:
        return False
    return True


def check_pid(pid):
    if len(pid) != 9:
        return False
    for char in pid: # May not need a for loop here
        if not char.isdigit():
            return False
    return True

def check_cid(cid):
    return True # https://knowyourmeme.com/memes/protegent-antivirus-yes


check_functions = {
    'byr': check_byr,
    'iyr': check_iyr,
    'eyr': check_eyr,
    'hgt': check_hgt,
    'hcl': check_hcl,
    'ecl': check_ecl,
    'pid': check_pid,
    'cid': check_cid
}


def find_passports(check, missing_inputs = {"cid"}):
    input_file = "input_04_day.txt"

    exp_inputs = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
    exp_inputs = exp_inputs - missing_inputs
    # exp_inputs = [x for x in exp_inputs if x not in missing_inputs]

    with open(input_file, "r") as file:

        found_params = {0}-{0}
        # https://stackoverflow.com/questions/6130374/empty-set-literal

        num_passports = 0
        line = file.readline()
        while line:
            if line == "\n":
                if exp_inputs - found_params == {0}-{0}:
                    num_passports += 1
                # print(exp_inputs - found_params)
                found_params = {0}-{0}
                line = file.readline()
                continue

            key_vals = line.split(" ")
            for pair in key_vals:
                key,val = pair.split(":")
                if check and check_functions[key](val.strip()): # .strip() 
                    found_params.add(key)

            prev_line = line
            line = file.readline()

        # One more check in case of end of file without "\n"
        if prev_line != "\n":
            if exp_inputs - found_params == {0}-{0}:
                num_passports += 1

    return num_passports

def day_04_challenge_part_1():
    return find_passports(check = False)

def day_04_challenge_part_2():
    return find_passports(check = True)


def main():
    # print("Day 4 Part 1: ", day_04_challenge_part_1())
    print("Day 4 Part 2: ", day_04_challenge_part_2())




if __name__ == "__main__":
    main()
