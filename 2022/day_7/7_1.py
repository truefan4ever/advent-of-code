from functools import reduce


def deep_get(dictionary: dict, keys: list, default=None):
    return reduce(
        lambda d, key: d.get(key, default) if isinstance(d, dict) else default,
        keys,
        dictionary,
    )


def calculate_total_size(dict_: dict) -> int:
    size = 0
    for key, value in dict_.items():
        size += calculate_total_size(value) if isinstance(value, dict) else value

    dict_["total"] = size
    return size


def get_nested_values(dict_: dict):
    for key, value in dict_.items():
        if isinstance(value, dict):
            yield from get_nested_values(value)
        elif key != "total":
            continue
        else:
            yield value


def main():
    with open("7.txt", "r") as f:
        data = f.read().split("\n")

        file_system = dict()
        current_path = []
        for line in data:
            split_line = line.split(" ")
            if "$" in split_line:
                if ".." in split_line:
                    current_path.pop(-1)
                elif "cd" in split_line:
                    # If folder doesn't exist
                    if deep_get(file_system, current_path).get(split_line[-1]) is None:
                        deep_get(file_system, current_path)[split_line[-1]] = {}
                    current_path.append(split_line[-1])
                else:
                    # ls
                    continue

            elif "dir" in split_line:
                # create empty dir
                deep_get(file_system, current_path)[split_line[-1]] = {}
            else:
                # file ["14848514", "b.txt"]
                deep_get(file_system, current_path)[split_line[-1]] = int(split_line[0])

        calculate_total_size(file_system)
        return sum(i for i in get_nested_values(file_system) if i < 100000)


if __name__ == "__main__":
    print(main())
