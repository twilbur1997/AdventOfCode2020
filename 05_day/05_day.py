def get_row_col_number(line):
    # FBBBBBBLRR
    # the first letter indicates whether the seat is in the front
    # (0 through 63) or the back (64 through 127).
    # F means to keep the lower half, while B means to keep the upper half.
    # For the last 3 letters,
    # L means to keep the lower half, while R means to keep the upper half.

    row_num = 0
    binary_add = 64
    for char in line[:8]: # first 7 characters
        if char == 'B':
            row_num += binary_add
        binary_add /= 2

    col_num = 0
    binary_add = 4
    for char in line[8:]: # rest of the characters
        if char == 'R':
            col_num += binary_add
        binary_add /= 2

    return row_num, col_num


def get_seat_ID(row, col):
    # Every seat also has a unique seat ID: multiply the row by 8,
    # then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.
    return row*8 + col


def day_05_challenge_part_1():
    input_file = "input_05_day.txt"

    highest_id = 0
    with open(input_file, "r") as file:
        line = file.readline().strip()
        while line:
            row, col = get_row_col_number(line)
            current_id = get_seat_ID(row, col)
            if current_id > highest_id:
                highest_id = current_id

            line = file.readline().strip()

    return highest_id


def main():
    print("Day 5 Part 1: ", day_05_challenge_part_1())
    # print("Day 5 Part 2: ", day_05_challenge_part_2())


if __name__ == "__main__":
    main()
