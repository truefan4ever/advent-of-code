import string

PRIORITY = {v: i + 1 for i, v in enumerate(string.ascii_lowercase)} | {v: i + 27 for i, v in enumerate(string.ascii_uppercase)}


def main():
    with open('3.txt', 'r') as f:
        data = [[rucksack[:len(rucksack//2)], rucksack[len(rucksack)//2:]] for rucksack in f.read().split('\n')]
        return calculate_priority(data=data)

def calculate_priority(data: list) -> int:
    common_items = []
    for rucksack in data:
        compartment_1, compartment_2 = rucksack
        common_item = set(compartment_1) & set(compartment_2)
        common_items.append(list(common_item)[0])
    
    # print(common_items)
    return sum([PRIORITY[item] for item in common_items])


if __name__ == "__main__":
    print(main())
