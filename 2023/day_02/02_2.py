import re


def main():
    with open("02.txt", "r") as f:
        result = []
        for line in f.read().split("\n"):
            _, sets = line.split(": ")
            colors_map = {
                "green": [],
                "red": [],
                "blue": [],
            }
            for num, color in re.compile(r"(\d+) (\w+)").findall(sets):
                colors_map[color].append(int(num))

            set_result = 1
            for i in [max(i) for i in colors_map.values()]:
                set_result *= i

            result.append(set_result)

        return sum(result)


if __name__ == "__main__":
    print(main())
