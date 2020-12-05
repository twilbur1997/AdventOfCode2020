"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""
# Passports are separated by blank lines.

def find_passports(missing_inputs = {"cid"}):
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
                found_params = {0}-{0}
                line = file.readline()
                continue

            key_vals = line.split(" ")
            for pair in key_vals:
                key = pair.split(":")[0]
                found_params.add(key)
            prev_line = line
            line = file.readline()
        if prev_line != "\n":
            if exp_inputs - found_params == {0}-{0}:
                num_passports += 1

    return num_passports

def day_04_challenge_part_1():
    return find_passports()


def main():
    print("Day 4 Part 1: ", day_04_challenge_part_1())
    # print("Day 4 Part 2: ", day_04_challenge_part_2())




if __name__ == "__main__":
    main()
