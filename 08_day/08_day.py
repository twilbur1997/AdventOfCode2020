def read_instructions():
    input_file = "input_08_day.txt"
    instructions = []

    with open(input_file, "r") as file:
        line = file.readline().strip()
        while line:
            instructions.append(line)
            line = file.readline().strip()

    return instructions

def day_08_challenge_part_1():
    instructions = read_instructions()



def main():
    print(day_08_challenge_part_1())
    # print(day_08_challenge_part_2())


if __name__ == "__main__":
    main()
