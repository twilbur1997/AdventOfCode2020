import os


def day_02_challenge_part_1():
    input_file = "input_02_day.txt"

    with open(input_file, "r") as file:
        # 7-8 k: hgcjkxhkskk
        line = file.readline().strip()
        num_passwords = 0

        while line:
            range_nums, letter, password = line.split(" ")

            min, max = range_nums.split("-")
            min = int(min)
            max = int(max)
            letter = letter[0]

            count = 0
            for chr in password:
                print(chr, " count: ", count, "\n")
                if chr == letter:
                    count += 1
            if count < min or count > max:
                # 1-3 a means it must contain a at least 1 time and at most 3 times
                num_passwords += 0
            else:
                num_passwords += 1

            line = file.readline().strip()

    return num_passwords


def main():
    print(day_02_challenge_part_1())


if __name__ == "__main__":
    main()
