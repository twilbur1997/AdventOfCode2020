def read_instructions():
    input_file = "input_08_day.txt"
    instructions = []

    with open(input_file, "r") as file:
        line = file.readline().strip()
        while line:
            instructions.append(line)
            line = file.readline().strip()

    return instructions


def process_instruction(line):
    command, number = line.split(" ")
    print(line.split(" "))
    number = int(number)
    return command, number


def day_08_challenge_part_1():
    instructions = read_instructions()
    count = 0
    accumulator = 0
    prev_counts = {0}-{0}
    while count < len(instructions):
        cmd, num = process_instruction(instructions[count])
        if count in prev_counts:
            return accumulator
        prev_counts.add(count)

        accumulator += num*(cmd == "acc")
        count += (num-1)*(cmd == "jmp")
        count += 1

    return 0


def main():
    print(day_08_challenge_part_1())
    # print(day_08_challenge_part_2())


if __name__ == "__main__":
    main()
