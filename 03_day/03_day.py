def day_03_challenge_part_1():
    input_file = "input_03_day.txt"

    with open(input_file, "r") as file:
        line = file.readline()
        width = len(line)-1

        num_trees = 0
        x_pos = 0
        while line:
            if line[x_pos] == "#":
                num_trees += 1

            x_pos = (x_pos + 3) % width
            line = file.readline()

    return num_trees


def find_trees(right_num = 1, down_num = 1):
    input_file = "input_03_day.txt"

    with open(input_file, "r") as file:
        line = file.readline()
        width = len(line)-1

        num_trees = 0
        x_pos = 0
        if line[x_pos] == "#":
            num_trees += 1

        x_pos = (x_pos + 3) % width
        line = file.readline()
        while line:
            if line[x_pos] == "#":
                num_trees += 1

            x_pos = (x_pos + 3) % width
            line = file.readline()

def day_03_challenge_part_2():
    """
    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
    """
    pairs_list = [(1,1), (3,1), (5,1), (7,1), (1,2)]



def main():
    print("Day 3 Part 1: ", day_03_challenge_part_1())
    # print("Day 3 Part 2: ", day_03_challenge_part_2())


if __name__ == "__main__":
    main()
