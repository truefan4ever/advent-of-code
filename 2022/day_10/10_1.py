def main():
    with open("10.txt", "r") as f:
        data = [line.split() for line in f.read().split("\n")]

    return count_signal_strengths(data)


def count_signal_strengths(instructions):
    cycle = 0
    register = 1
    strengths = 0
    for instruction in instructions:
        if len(instruction) == 1:
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                strengths += cycle * register

            continue

        for i in range(1, 3):
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                strengths += cycle * register

            if i == 2:
                register += int(instruction[-1])

    return strengths


if __name__ == "__main__":
    print(main())
