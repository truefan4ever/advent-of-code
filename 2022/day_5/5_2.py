from collections import deque


def chunks(iterable, chunk_size):
    chunk = ""

    for item in iterable:
        if len(chunk) >= chunk_size:
            yield chunk
            chunk = item
        else:
            chunk += item

    if chunk:
        yield chunk


def main():
    with open("5.txt", "r") as f:
        data = [pair for pair in f.read().split("\n")]
        stack_lines = []
        moves = []
        for index, value in enumerate(data):
            if "[" in value:
                stack_lines.append(data[index])
            elif "move" in value:
                moves.append(data[index])

        # Get number of stacks
        stack_number = int(max(data[len(stack_lines)].replace(" ", "")))

        # Remove redundant symbols
        stack_lines = [
            [
                c.replace("[", "").replace("] ", "").replace("]", "")
                if "   " not in c
                else None
                for c in chunks(line, 4)
            ]
            for line in stack_lines
        ]

        # Get deques
        deques = [deque() for _ in range(stack_number)]
        for line in stack_lines[::-1]:
            for index, crate in enumerate(line):
                if crate:
                    deques[index].append(crate)

        # Get parsed moves
        parsed_moves = []
        for move in moves:
            parsed_move = []
            for el in move.split():
                try:
                    parsed_move.append(int(el))
                except ValueError:
                    pass

            parsed_moves.append(parsed_move)

        return move_crates(deques, parsed_moves)


def move_crates(data, moves):
    # Apply moves
    for move in moves:
        num_of_crates, from_index, to_index = move
        buffer = [data[from_index - 1].pop() for _ in range(num_of_crates)]

        for el in buffer[::-1]:
            data[to_index - 1].append(el)

    # Get top items
    message = ""
    for d in data:
        try:
            message += d.pop()
        except IndexError:
            continue

    return message


if __name__ == "__main__":
    print(main())
