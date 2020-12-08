import copy


def generate_luggage():
    input_file = "input_07_day.txt"

    with open(input_file, "r") as file:
        line = file.readline().strip()

        luggage_dict = {}
        while line:
            contain_split = line.split("contain")
            parent_words = contain_split[0].split(" ")
            parent = parent_words[0]+" "+parent_words[1]

            children_words = contain_split[1].split(",")
            children = []
            for ch_phrase in children_words:
                ch_phrase = ch_phrase.strip().split(" ")

                # drab tan bags contain no other bags.
                if ch_phrase[0] == 'no':
                    break

                number = int(ch_phrase[0])
                child = ch_phrase[1]+" "+ch_phrase[2]
                children.append((number, child))

            luggage_dict[parent] = children
            line = file.readline().strip()
    return luggage_dict


def start_recurse_bags(luggage, find_bag):
    # Find how many parent bags can eventually fit "find_bag"
    total_bags = 0
    for parent_bag in luggage.keys():
        total_bags += recurse_bags(luggage, parent_bag, find_bag)
        print(total_bags)

    return total_bags


def recurse_bags(luggage, parent_bag, find_bag):
    total = 0
    if parent_bag not in luggage: # due to del later, doesn't affect top level
        return 0
    children_bags = luggage[parent_bag]
    for pair in children_bags:
        if pair[1] == find_bag:
            return 1

        # prevent infinite loops
        # luggage2 = copy.deepcopy(luggage)
        # del luggage2[parent_bag]
        total += recurse_bags(luggage2, pair[1], find_bag)

    return (total > 0)


def day_07_challenge_part_1(input_bag):
    luggage_dict = generate_luggage()
    return start_recurse_bags(luggage_dict, input_bag)


def main():
    print(day_07_challenge_part_1("shiny gold"))


if __name__ == "__main__":
    main()
