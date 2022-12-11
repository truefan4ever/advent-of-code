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


def move_tail(h_position: tuple, t_position: tuple) -> tuple:
    x_axis_diff = abs(h_position[1] - t_position[1])
    y_axis_diff = abs(h_position[0] - t_position[0])

    if x_axis_diff <= 1 and y_axis_diff <= 1:
        return t_position

    if x_axis_diff == 2:
        # Use axis y from head and move tail along x
        return h_position[0], t_position[1] + 1 if h_position[1] > t_position[1] else t_position[1] - 1
    if y_axis_diff == 2:
        # Use axis x from head and move tail along y
        return t_position[0] + 1 if h_position[0] > t_position[0] else t_position[0] - 1, h_position[1]


def simulate_motions(routes: list):
    # Start position
    current_h_position = (0, 0)
    current_t_position = (0, 0)

    tail_positions = set()

    for route in routes:
        direction, num_of_moves = route
        y, x = MOVES[direction]
        for _ in range(int(num_of_moves)):
            # Set current head position
            current_h_position = (current_h_position[0] + y, current_h_position[1] + x)

            # Set current tail position
            current_t_position = move_tail(h_position=current_h_position, t_position=current_t_position)

            tail_positions.add(current_t_position)

    return len(tail_positions)


if __name__ == "__main__":
    print(main())
