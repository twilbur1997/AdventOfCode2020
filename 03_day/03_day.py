import os


def day_03_challenge_part_1():
    input_file = "input_03_day.txt"

    with open(input_file, "r") as file:
        prev_lines = []
        line = int(file.readline().strip())

        while line:
            prev_lines.append(line)
            line = int(file.readline().strip())

    return 0
    

def main():
    print(day_03_challenge_part_1())
    

if __name__ == "__main__":
    main()