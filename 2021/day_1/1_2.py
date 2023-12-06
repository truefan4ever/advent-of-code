def main():
    with open("1.txt", "r") as f:
        data = [int(i) for i in f.read().split("\n")]

    transformed_data = transform_data(data)
    print(count_increases(transformed_data))


def transform_data(data: list) -> list:
    transformed_data = []
    for i, v in enumerate(data):
        try:
            d = [data[i], data[i + 1], data[i + 2]]
        except IndexError:
            break

        transformed_data.append(d)

    summed_data = [sum(i) for i in transformed_data]

    return summed_data


def count_increases(data: list) -> int:
    counter = 0
    val = 0
    for element in data:
        if element > val:
            counter += 1

        val = element

    return counter - 1


if __name__ == "__main__":
    main()
