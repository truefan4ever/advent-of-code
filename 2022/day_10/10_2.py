def main():
    with open('10.txt', 'r') as f:
        data = [line.split() for line in f.read().split('\n')]

    return count_signal_strengths(data)


def get_position_on_crt(elements_in_row: int, id_: int) -> tuple:
    column = id_ % elements_in_row
    row = id_ // elements_in_row + 1 if column else id_ // elements_in_row
    # To index from 0
    return row - 1, column - 1


def draw_pixel(crt: list, cycle: int, register: int):
    row_len = len(crt[0])
    # To index from 1
    sprite_middle_id = register + 1
    sprite_pixel_2 = get_position_on_crt(row_len, sprite_middle_id)
    drawing_p = get_position_on_crt(row_len, cycle)

    sprite_pixel_1_x = sprite_pixel_2[1] - 1
    sprite_pixel_3_x = sprite_pixel_2[1] + 1 if sprite_pixel_2[1] + 1 < row_len else 0
    # Check only X-axis
    if drawing_p[1] in [sprite_pixel_1_x, sprite_pixel_2[1], sprite_pixel_3_x]:
        crt[drawing_p[0]][drawing_p[1]] = "#"


def count_signal_strengths(instructions):
    cycle = 0
    register = 1

    crt = [["." for _ in range(40)] for _ in range(6)]

    for instruction in instructions:
        if len(instruction) == 1:
            cycle += 1
            draw_pixel(crt=crt, cycle=cycle, register=register)
            continue

        for i in range(1, 3):
            cycle += 1
            draw_pixel(crt=crt, cycle=cycle, register=register)
            if i == 2:
                register += int(instruction[-1])

    return ["".join(row) for row in crt]


if __name__ == "__main__":
    print(main())
