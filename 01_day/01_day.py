import os


def day_1_challenge_part_1():
    input_file = "input_01_day.txt"

    with open(input_file, "r") as file:
        prev_lines = []
        line = int(file.readline().strip())
        while line:
            for prev in prev_lines:
                if line + prev == 2020:
                    return line*prev

            prev_lines.append(line)
            line = int(file.readline().strip())

    return 0

def day_1_challenge_part_2():
    input_file = "input_01_day.txt"

    with open(input_file, "r") as file:
        prev_lines = []
        line = int(file.readline().strip())
        while line:
            for prev in prev_lines:
                for prev2 in prev_lines:
                    if prev2 != prev:
                        if line + prev + prev2 == 2020:
                            return line*prev*prev2

            prev_lines.append(line)
            line = int(file.readline().strip())

    return 0


def main():
    # print(day_1_challenge_part_1())
    print(day_1_challenge_part_2())



if __name__ == "__main__":
    main()
