def get_cmd_num(line):
    command, number = line.split(" ")
    # print(line.split(" "))
    number = int(number)
    return command, number


def day_08_challenge_part_1():
    instructions = [line.strip() for line in open('input_08_day.txt', 'r')]
    count = 0
    accumulator = 0
    prev_counts = {0}-{0}
    while count < len(instructions):
        # print("Count: ", count)
        # print("Acc: ", accumulator)
        cmd, num = get_cmd_num(instructions[count])

        if count in prev_counts:
            return accumulator
        prev_counts.add(count)

        accumulator += num*(cmd == "acc")
        count += num*(cmd == "jmp")
        count += (cmd != "jmp")

    return 0

def day_08_challenge_part_2():
    instructions = [line.strip() for line in open('input_08_day.txt', 'r')]
    count = 0
    accumulator = 0
    prev_counts = {0}-{0}
    while count < len(instructions):
        cmd, num = get_cmd_num(instructions[count])

        if count in prev_counts:
            break
        prev_counts.add(count)

        accumulator += num*(cmd == "acc")
        count += num*(cmd == "jmp")
        count += (cmd != "jmp")

    for prev in prev_counts:
        count = 0
        accumulator = 0
        prev_counts_2 = {0}-{0}
        while count < len(instructions):
            cmd, num = get_cmd_num(instructions[count])

            # Let's try switching the command that we already ran earlier
            if count == prev and cmd != "acc":
                # value_if_true if condition else value_if_false
                cmd = "nop" if cmd == "jmp" else "jmp"

            if count in prev_counts_2:
                break
            prev_counts_2.add(count)

            accumulator += num*(cmd == "acc")
            count += num*(cmd == "jmp")
            count += (cmd != "jmp")

        if count in prev_counts_2:
            continue
        else:
            print(count)
            print(len(instructions))
            print(accumulator)


def main():
    # print(day_08_challenge_part_1())
    print(day_08_challenge_part_2())


if __name__ == "__main__":
    main()
