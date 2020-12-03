def day_03_challenge_part_1():
    input_file = "input_03_day.txt"

    with open(input_file, "r") as file:
        # ......#..##..#...#...#.###.....
        # following a slope of right 3 and down 1,
        # how many trees would you encounter?
        line = file.readline() # skip first line
        width = len(line)

        num_trees = 0
        x_pos = 0

        x_pos = (x_pos + 3) % width
        line = file.readline()
        while line:
            if line[x_pos] == "#":
                num_trees += 1

            x_pos = (x_pos + 3) % width
            line = file.readline()

    return num_trees


def main():
    print("Day 3 Part 1: ", day_03_challenge_part_1())
    # print("Day 3 Part 2: ", day_03_challenge_part_2())


if __name__ == "__main__":
    main()
