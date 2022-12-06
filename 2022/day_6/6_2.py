def main() -> int:
    with open('6.txt', 'r') as f:
        data = f.read().split('\n')[0]
        return find_start_marker(data)


def find_start_marker(data: str) -> int:
    buffer = []
    for index, el in enumerate(data):
        if len(buffer) == 14:
            if len(set(buffer)) == 14:
                # Since index in this sequense should be from 1 to ... 
                return (index - 1) + 1
            else:
                buffer.pop(0)

        buffer.append(el)

if __name__ == "__main__":
    print(main())