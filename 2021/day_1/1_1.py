def main():
    with open('1.txt', 'r') as f:
        data = [int(i) for i in f.read().split('\n')]

    counter = count_increases(data)
    print(counter)


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
