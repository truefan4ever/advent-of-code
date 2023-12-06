SYMBOLS_TO_IGNORE = ".0123456789"


def main():
    with open('03.txt', 'r') as f:
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
                        # top left
                        if line_id > 0 and digit_id > 0 and matrix[line_id - 1][digit_id - 1] not in SYMBOLS_TO_IGNORE:
                            add = True
                            continue

                        # top
                        if line_id > 0 and matrix[line_id - 1][digit_id] not in SYMBOLS_TO_IGNORE:
                            add = True
                            continue

                        # left
                        if digit_id > 0 and matrix[line_id][digit_id - 1] not in SYMBOLS_TO_IGNORE:
                            add = True
                            continue

                        # bottom left
                        if line_id + 1 < len(matrix) and digit_id > 0 and matrix[line_id + 1][digit_id - 1] not in SYMBOLS_TO_IGNORE:
                            add = True
                            continue

                        # bottom
                        if line_id + 1 < len(matrix) and matrix[line_id + 1][digit_id] not in SYMBOLS_TO_IGNORE:
                            add = True
                            continue

                        # top right
                        if line_id > 0 and digit_id + 1 < len(line) and matrix[line_id - 1][digit_id + 1] not in SYMBOLS_TO_IGNORE:
                            add = True
                            continue

                        # right
                        if digit_id + 1 < len(line) and matrix[line_id][digit_id + 1] not in SYMBOLS_TO_IGNORE:
                            add = True
                            continue

                        # bottom right
                        if line_id + 1 < len(matrix) and digit_id + 1 < len(line) and matrix[line_id + 1][digit_id + 1] not in SYMBOLS_TO_IGNORE:
                            add = True
                            continue

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
