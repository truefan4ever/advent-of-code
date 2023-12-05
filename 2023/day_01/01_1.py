def main():
    with open('01.txt', 'r') as f:
        return sum(
            int(f"{digits[0]}{digits[-1]}")
            for i in f.read().split("\n")
            if (digits := [d for d in i if d.isdigit()])
        )


if __name__ == "__main__":
    print(main())
