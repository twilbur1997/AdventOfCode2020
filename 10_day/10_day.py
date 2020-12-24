def day_10_challenge_part_1():
    num_list = [int(line.strip()) for line in open('input_10_day.txt', 'r')]

    num_list.sort()
    prev_num = 0
    count_list = [0, 0, 1] # 1, 2, and 3
    for num in num_list:
        diff = num - prev_num
        count_list[diff-1] += 1

        prev_num = num

    return count_list[0]*count_list[2]


def main():
    print(day_10_challenge_part_1())


if __name__ == "__main__":
    main()
