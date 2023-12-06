def main():
    with open("1.txt", "r") as f:
        data = [[int(i) for i in elf.split("\n")] for elf in f.read().split("\n\n")]
        return count_calories(data=data)


def count_calories(data: list) -> int:
    total_per_elf = [sum(elf) for elf in data]
    total_per_elf.sort(reverse=True)
    return sum(total_per_elf[:3])


if __name__ == "__main__":
    print(main())
