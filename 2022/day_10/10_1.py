def main():
    with open('10.txt', 'r') as f:
        data = [line.split() for line in f.read().split('\n')]

    return foo(data)


def foo(instructions):
    cycle = 0
    register = 1
    strengths = []
    for instruction in instructions:
        if len(instruction) == 1:
            cycle += 1
            strengths.append(cycle * register)
            continue

        for i in range(1, 3):
            cycle += 1
            strengths.append(cycle * register)
            if i == 2:
                register += int(instruction[-1])

    return sum([strengths[19], strengths[59], strengths[99], strengths[139], strengths[179], strengths[219]])


if __name__ == "__main__":
    print(main())
