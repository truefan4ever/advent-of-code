def main():
    with open('4.txt', 'r') as f:
        data = [pair for pair in f.read().split('\n')]
        ranges = []
        for pair in data:
            modified_pair = []
            for elf in pair.split(','):
                start_index, stop_index = elf.split('-')
                modified_pair.append({i for i in range(int(start_index), int(stop_index) + 1)})

            ranges.append(modified_pair)

        return count_pairs(ranges)


def count_pairs(data: list) -> int:
    counter = 0
    for pair in data:
        elf_1_range, elf_2_range = pair
        if elf_1_range.issubset(elf_2_range) or elf_2_range.issubset(elf_1_range):
            counter +=1

    return counter

if __name__ == "__main__":
    print(main())
