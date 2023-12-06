def main():
    with open("1.txt", "r") as f:
        data = [[int(i) for i in elf.split("\n")] for elf in f.read().split("\n\n")]
        return count_calories(data=data)


def count_calories(data: list) -> int:
    return max([sum(elf) for elf in data])


if __name__ == "__main__":
    print(main())
