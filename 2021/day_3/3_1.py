def main():
    with open('3.txt', 'r') as f:
        data = f.read().split('\n')

    gamma, epsilon = transform_data(data)
    print(int(gamma, 2) * int(epsilon, 2))


def transform_data(data: list):
    transformed_data = []
    for i, _ in enumerate(data[0]):
        d = [int(j[i]) for j in data]
        transformed_data.append(d)

    gamma = ''
    for i in transformed_data:
        most_common_bit = max(set(i), key=i.count)
        gamma += str(most_common_bit)

    epsilon = ''
    for i in gamma:
        epsilon += str(int(i) ^ 1)

    return gamma, epsilon


if __name__ == "__main__":
    main()
