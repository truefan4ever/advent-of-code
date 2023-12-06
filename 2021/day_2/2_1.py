def main():
    with open("2.txt", "r") as f:
        data = f.read().split("\n")

    position, depth = calculate_position(data)
    print(position, depth)
    print(position * depth)


def calculate_position(data: list) -> int:
    position = 0
    depth = 0
    for element in data:
        action, val = element.split(" ")
        if action == "forward":
            position += int(val)
        elif action == "down":
            depth += int(val)
        elif action == "up":
            depth -= int(val)

    return position, depth


if __name__ == "__main__":
    main()
