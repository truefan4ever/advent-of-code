def main():
    with open("3.txt", "r") as f:
        data = f.read().split("\n")

    ox_rating = get_rating(data, "most")
    co2_rating = get_rating(data, "least")
    print(int(ox_rating, 2) * int(co2_rating, 2))


def count_bits(bits, state):
    one_count = 0
    zero_count = 0
    for b in bits:
        if b == 1:
            one_count += 1
        elif b == 0:
            zero_count += 1

    if state == "most":
        if one_count == zero_count:
            return 1
        elif one_count > zero_count:
            return 1
        elif one_count < zero_count:
            return 0

    elif state == "least":
        if one_count == zero_count:
            return 0
        elif one_count > zero_count:
            return 0
        elif one_count < zero_count:
            return 1


def get_elms(lst, index, value):
    a = []
    for el in lst:
        if el[index] == str(value):
            a.append(el)

    return a


def get_rating(raw_data: list, state: str):
    for i, _ in enumerate(raw_data[0]):
        bits = [int(j[i]) for j in raw_data]
        most_common_bit = count_bits(bits, state)
        raw_data = get_elms(raw_data, i, most_common_bit)
        # print(raw_data)
        if len(raw_data) == 1:
            break

    return raw_data[0]


if __name__ == "__main__":
    main()
