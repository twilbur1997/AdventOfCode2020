def get_neighbors(x_coord, y_coord, seat_list):
    # NW, N, NE, E, SE, S, SW, W
    total = 0

    if y_coord > 0:
        if x_coord > 0:
            total += (seat_list[y_coord-1][x_coord-1] == "#")
        total += (seat_list[y_coord-1][x_coord] == "#")
        if x_coord < len(seat_list[y_coord-1])-1:
            total += (seat_list[y_coord-1][x_coord+1] == "#")

    if x_coord > 0:
        total += (seat_list[y_coord][x_coord-1] == "#")
    # total += (seat_list[y_coord][x_coord] == "#") # Nope, isn't a neighbor
    if x_coord < len(seat_list[y_coord])-1:
        total += (seat_list[y_coord][x_coord+1] == "#")

    if y_coord < len(seat_list)-1:
        if x_coord > 0:
            total += (seat_list[y_coord+1][x_coord-1] == "#")
        total += (seat_list[y_coord+1][x_coord] == "#")
        if x_coord < len(seat_list[y_coord+1])-1:
            total += (seat_list[y_coord+1][x_coord+1] == "#")
    return total


def change_seat_status(x_coord, y_coord, seat_list, occupied_status):
    neighbors = get_neighbors(x_coord, y_coord, seat_list)
    if occupied_status and neighbors >= 4:
        return True
    elif not occupied_status and neighbors == 0:
        return True
    return False


def day_11_challenge_part_1():
    seat_list = [line.strip() for line in open('input_11_day.txt', 'r')]

    new_seats = []
    y_coord = 0
    seats_changing = True
    while seats_changing:
        for seat_string in seat_list:
            new_seat_string = []
            x_coord = 0
            for seat in seat_string:
                if seat == ".":
                    new_seats.append(".")

                elif seat == "L":
                    if change_seat_status(x_coord, y_coord, seat_list, False):
                        new_seats.append("#")
                    else:
                        new_seats.append("L")

                elif seat == "#":
                    if change_seat_status(x_coord, y_coord, seat_list, True):
                        new_seats.append("L")
                    else:
                        new_seats.append("#")

                x_coord += 1
            new_seats.append(new_seat_string)

            y_coord += 1
        seats_changing = False
        for seat_str_new, seat_str_old in zip(new_seats, seat_list):
            if seat_str_new != seat_str_old:
                seat_list = new_seats
                seats_changing = True
                continue
        break

    total_occupied = 0
    for seat_str in new_seats:
        for seat in seat_string:
            if seat == "#":
                total_occupied += 1

    return total_occupied


def main():
    print(day_11_challenge_part_1())


if __name__ == "__main__":
    main()
