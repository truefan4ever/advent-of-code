MAP = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0,
}


def main():
    with open('01.txt', 'r') as f:
        result = []
        for line in f.read().split("\n"):
            substring = ""
            digits = []
            for symbol in line:
                if symbol.isdigit():
                    digits.append(symbol)
                    substring = ""
                    continue

                if symbol.isalpha():
                    substring += symbol
                    if any(key.startswith(substring) for key in MAP.keys()):
                        if substring in MAP.keys():
                            digits.append(str(MAP[substring]))
                            substring = symbol if any(substring.endswith(i) for i in "eont") else ""
                    else:
                        substring = "" if substring == symbol else substring[1:]

            result.append(int(f"{digits[0]}{digits[-1]}"))
        
        print(result)
        return sum(result)


if __name__ == "__main__":
    print(main())
