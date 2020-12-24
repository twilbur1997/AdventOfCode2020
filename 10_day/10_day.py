from itertools import combinations


def day_10_challenge_part_1():
    num_list = [int(line.strip()) for line in open('input_10_day.txt', 'r')]
    num_list.sort()
    # num_list.insert(0,0) # outlet not needed???
    num_list.append(num_list[-1]+3) # devices

    prev_num = 0
    count_list = [0, 0, 0] # 1, 2, and 3
    for num in num_list:
        diff = num - prev_num
        count_list[diff-1] += 1

        prev_num = num

    return count_list[0]*count_list[2]


def check_good(num_list, skip_nums):
    prev_num = 0
    for num in num_list:
        if num in skip_nums:
            continue
        diff = num - prev_num
        if diff > 3:
            return False
        prev_num = num
    return True

def get_all_combinations(skip_indices, max_r):
    all_combos = []
    for x in range(max_r-1):
        print(x)
        all_combos.extend(combinations(skip_indices, x+1))

    return all_combos


def day_10_challenge_part_2():
    num_list = [int(line.strip()) for line in open('input_10_day.txt', 'r')]
    num_list.sort()
    num_list.insert(0,0)
    num_list.append(num_list[-1]+3)

    total_combos = 0
    # skip_indices = [0, 1, 2] # Error: a max of three skipped adapters
    skip_indices = list(range(1, len(num_list)-1))

    for x in range(len(skip_indices)-1):
        combinations(skip_indices, x+1)
    for ind_combo in get_all_combinations(skip_indices, len(skip_indices)):
        if total_combos % 20:
            print(total_combos)
        skip_nums = [num_list[ind] for ind in ind_combo]
        total_combos += check_good(num_list, skip_nums)

    return total_combos


def main():
    print(day_10_challenge_part_1())
    print(day_10_challenge_part_2())


if __name__ == "__main__":
    main()
