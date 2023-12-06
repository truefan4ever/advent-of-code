import re

MAP = {
    "green": 13,
    "red": 12,
    "blue": 14,
}


def main():
    with open('02.txt', 'r') as f:
        result = []
        for line in f.read().split("\n"):
            game, sets = line.split(": ")
            result.append(int(game.split(" ")[-1]))

            for num, color in re.compile(r'(\d+) (\w+)').findall(sets):
                if MAP[color] < int(num):
                    result.pop()
                    break

        return sum(result)


if __name__ == "__main__":
    print(main())
