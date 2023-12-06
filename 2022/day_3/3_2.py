import string

PRIORITY = {v: i + 1 for i, v in enumerate(string.ascii_lowercase)} | {
    v: i + 27 for i, v in enumerate(string.ascii_uppercase)
}


def chunks(iterable, chunk_size):
    """
    chunk function that also works with generators
    """
    chunk = []

    for item in iterable:
        if len(chunk) >= chunk_size:
            yield chunk
            chunk = [item]
        else:
            chunk.append(item)

    if chunk:
        yield chunk


def main():
    with open("3.txt", "r") as f:
        data = [c for c in chunks([rucksack for rucksack in f.read().split("\n")], 3)]
        return calculate_priority(data=data)


def calculate_priority(data: list) -> int:
    common_items = []
    for group_ in data:
        elf_1, elf_2, elf_3 = group_
        common_item = set(elf_1) & set(elf_2) & set(elf_3)
        common_items.append(list(common_item)[0])

    return sum([PRIORITY[item] for item in common_items])


if __name__ == "__main__":
    print(main())
