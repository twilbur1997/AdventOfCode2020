def check_sum(preamble_numlist, current_num):
    for num1 in preamble_numlist:
        for num2 in preamble_numlist:
            if ((num1 + num2) == current_num) and num1 != num2:
                return True
    return False


def day_09_challenge_part_1():
    num_list = [int(line.strip()) for line in open('input_09_day.txt', 'r')]

    preamble = 25
    index = preamble
    preamble_numlist = num_list[index-preamble:index]

    while index < (len(num_list)):
        preamble_numlist = num_list[index-preamble:index]
        current_num = num_list[index]
        if not check_sum(preamble_numlist, current_num):
            return current_num

        index += 1

    return 0


def day_09_challenge_part_2():


def main():
    print(day_09_challenge_part_1())
    invalid_num = day_09_challenge_part_1()
    print(day_09_challenge_part_2(invalid_num))


if __name__ == "__main__":
    main()
