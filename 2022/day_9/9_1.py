from contextlib import suppress


MOVES = {
    # y, x
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0),
}


def main():
    with open('9.txt', 'r') as f:
        data = [line.split(" ") for line in f.read().split('\n')]

    return simulate_motions(data)


def is_needed_to_move_tail(field, h_position) -> bool:
    """Returns if the tail should be moved and if the tail should be moved diagonally next step"""
    index_error_suppressed = suppress(IndexError)

    # H covers T
    with index_error_suppressed:
        if field[h_position[0]][h_position[1]].get("T"):
            return False

    # TH
    with index_error_suppressed:
        if field[h_position[0]][h_position[1] - 1].get("T"):
            return False

    # HT
    with index_error_suppressed:
        if field[h_position[0]][h_position[1] + 1].get("T"):
            return False

    # T
    # H
    with index_error_suppressed:
        if field[h_position[0] - 1][h_position[1]].get("T"):
            return False

    # H
    # T
    with index_error_suppressed:
        if field[h_position[0] + 1][h_position[1]].get("T"):
            return False

    #  H
    # T
    with index_error_suppressed:
        if field[h_position[0] + 1][h_position[1] - 1].get("T"):
            return False

    # H
    #  T
    with index_error_suppressed:
        if field[h_position[0] + 1][h_position[1] + 1].get("T"):
            return False

    #  T
    # H
    with index_error_suppressed:
        if field[h_position[0] - 1][h_position[1] + 1].get("T"):
            return False

    # T
    #  H
    with index_error_suppressed:
        if field[h_position[0] - 1][h_position[1] - 1].get("T"):
            return False

    return True


def get_tail_coordinates_for_movement(current_h_position: list, current_t_position: list) -> tuple:
    x_axis_diff = current_h_position[1] - current_t_position[1]
    y_axis_diff = current_h_position[0] - current_t_position[0]

    # If the head and tail aren't in the same row or column it is diagonal movement
    # And the difference between x-axes is 2 it's needed to use head's y coordinate
    if x_axis_diff and y_axis_diff and x_axis_diff % 2 == 0:
        return current_h_position[0], current_t_position[1]
    # The difference between y-axes is 2 it's needed to use head's x coordinate
    elif x_axis_diff and y_axis_diff and y_axis_diff % 2 == 0:
        return current_t_position[0], current_h_position[1]
    else:
        # Use tail's coordinates
        return current_t_position[0], current_t_position[1]


def simulate_motions(routes: list):
    field = [[dict() for _ in range(500)] for _ in range(500)]

    # Start position
    field[250][250].update({"H": True, "T": True, "s": True, "count": 1})
    current_h_position = [250, 250]
    current_t_position = [250, 250]

    for route in routes:
        direction, num_of_moves = route
        y, x = MOVES[direction]
        for _ in range(int(num_of_moves)):
            # Remove head
            field[current_h_position[0]][current_h_position[1]].pop("H")

            # Move head
            field[current_h_position[0] + y][current_h_position[1] + x].update({"H": True})

            # Set current head position
            current_h_position = [current_h_position[0] + y, current_h_position[1] + x]

            if is_needed_to_move_tail(field=field, h_position=current_h_position):
                # Remove tail
                field[current_t_position[0]][current_t_position[1]].pop("T")

                tail_y, tail_x = get_tail_coordinates_for_movement(
                    current_h_position=current_h_position,
                    current_t_position=current_t_position,
                )

                # Move tail
                field[tail_y + y][tail_x + x].update({"T": True})

                # Count tail
                if not field[tail_y + y][tail_x + x].get("count"):
                    field[tail_y + y][tail_x + x]["count"] = 1
                else:
                    field[tail_y + y][tail_x + x]["count"] += 1

                # Set current tail position
                current_t_position = [tail_y + y, tail_x + x]

    counter = 0
    for row in field:
        for element in row:
            if element.get("count"):
                counter += 1

    return counter


if __name__ == "__main__":
    print(main())
