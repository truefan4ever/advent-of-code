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
        for i in f.read().split("\n"):
            substring = ""
            digits = []
            for s in i:
                if s.isdigit():
                    digits.append(s)
                    substring = ""
                    continue

                if s.isalpha():
                    substring += s
                    if any(key.startswith(substring) for key in MAP.keys()):
                        if substring in MAP.keys():
                            digits.append(str(MAP[substring]))
                            substring = s if any(substring.endswith(i) for i in "eon") else ""
                    else:
                        substring = "" if substring == s else s

            result.append(int(f"{digits[0]}{digits[-1]}"))
        
        print(result)
        return sum(result)


if __name__ == "__main__":
    print(main())
