SYMBOLS_TO_IGNORE = ".0123456789"


def main():
    with open("03.txt", "r") as f:
        result = []
        matrix = [line for line in f.read().split("\n")]
        for line_id, line in enumerate(matrix):
            buffer = []
            num = ""
            add = False
            neg = False
            for digit_id, digit in enumerate(line):
                if digit.isdigit():
                    num += digit
                    if not add:
                        for line_index in (-1, 0, 1):
                            for digit_index in (-1, 0, 1):
                                if (
                                    0 <= line_id + line_index < len(matrix)
                                    and 0 < digit_id + digit_index < len(line)
                                    and matrix[line_id + line_index][
                                        digit_id + digit_index
                                    ]
                                    not in SYMBOLS_TO_IGNORE
                                ):
                                    add = True
                                    break

                else:
                    if num and add:
                        if neg:
                            num = f"-{num}"
                        buffer.append(int(num))

                    num = ""
                    add = False
                    neg = False

            if num and add:
                if neg:
                    num = f"-{num}"
                buffer.append(int(num))

            result.extend(buffer)

        return sum(result)


if __name__ == "__main__":
    print(main())
