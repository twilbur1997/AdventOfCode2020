import os


def day_01_challenge_part_1():
    input_file = "input_01_day.txt"

    with open(input_file, "r") as file:
        prev_lines = []
        line = int(file.readline().strip())
        while line:
            for prev_num in prev_lines:
                if line + prev_num == 2020:
                    return line*prev_num

            prev_lines.append(line)
            line = int(file.readline().strip())

    return 0

def day_01_challenge_part_2():
    # bug: doesn't work for repeated numbers, such as 2000, 10, 10
    input_file = "input_01_day.txt"

    with open(input_file, "r") as file:
        prev = []
        line = int(file.readline().strip())
        while line:
            for prev1_i in range(len(prev)):
                for prev2_i in range(len(prev)):
                    if prev1_i != prev2_i:
                        if line+prev[prev1_i]+prev[prev2_i] == 2020:
                            return line*prev[prev1_i]*prev[prev2_i]

            prev.append(line)
            line = int(file.readline().strip())

    return 0


def main():
    print("Day 1 Part 1: ", day_01_challenge_part_1())
    print("Day 1 Part 2: ", day_01_challenge_part_2())




if __name__ == "__main__":
    main()
