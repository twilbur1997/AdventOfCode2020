def day_06_challenge_part_1():
    input_file = "input_06_day.txt"

    with open(input_file, "r") as file:
        line = file.readline()
        num_questions = 0
        family_set = {0}-{0}
        while line:
            if line == "\n":
                num_questions += len(family_set)
                family_set = {0}-{0}
            else:
                for char in line.strip():
                    family_set.add(char)

            prev_line = line
            line = file.readline()

        # One more check in case of end of file without "\n"
        if prev_line != "\n":
            num_questions += len(family_set)

    return num_questions


def day_06_challenge_part_2():
    input_file = "input_06_day.txt"

    with open(input_file, "r") as file:
        line = file.readline()
        num_questions = 0
        family_set = {0}-{0}
        prev_line = 0
        while line:
            if line == "\n":
                num_questions += len(family_set)
                print(len(family_set), "\n\n")
                family_set = {0}-{0}
            else:
                indiv_set = {0}-{0}
                for char in line.strip():
                    indiv_set.add(char)
                if prev_line == "\n" or prev_line == 0:
                    family_set = indiv_set
                else:
                    family_set = family_set.intersection(indiv_set)

            prev_line = line
            line = file.readline()

        # One more check in case of end of file without "\n"
        if prev_line != "\n":
            num_questions += len(family_set)

    return num_questions



def main():
    print("Day 6 Part 1: ", day_06_challenge_part_1())
    print("Day 6 Part 2: ", day_06_challenge_part_2())



if __name__ == "__main__":
    main()
