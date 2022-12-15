def main():
    with open('11.txt', 'r') as f:
        data = [line for line in f.read().split('\n')]

    monkeys_items = [line.split(": ")[1].split(", ") for line in data if "Starting" in line]
    monkeys_items = [[int(item) for item in monkey] for monkey in monkeys_items]
    total_items_per_monkey = [0 for _ in monkeys_items]
    operations = [line.split("= ")[1].split(" ") for line in data if "Operation" in line]
    tests = [int(line.split("by ")[1]) for line in data if "Test" in line]
    true_decisions = [int(line.split("monkey ")[1]) for line in data if "true" in line]
    false_decisions = [int(line.split("monkey ")[1]) for line in data if "false" in line]

    # Trick with a common multiple of all monkeys' divisors
    # Perform a modulo (%) to each item.
    modulo = 1
    for div in tests:
        modulo *= div

    for _ in range(10000):
        play_round(
            monkeys_items=monkeys_items,
            operations=operations,
            tests=tests,
            true_decisions=true_decisions,
            false_decisions=false_decisions,
            total_items_per_monkey=total_items_per_monkey,
            modulo=modulo,
        )

    inspections_count = sorted(total_items_per_monkey, reverse=True)[:2]
    print(inspections_count[0] * inspections_count[1])


def play_round(monkeys_items: list, operations: list, tests: list, true_decisions: list, false_decisions: list, total_items_per_monkey: list, modulo: int):
    for monkey_id, monkey in enumerate(monkeys_items):
        processed_count = total_items_per_monkey[monkey_id]
        for _ in range(len(monkey)):
            item = monkey.pop(0)
            processed_count += 1
            operation = operations[monkey_id]
            second_value = item if operation[-1] == "old" else int(operation[-1])
            # Calculate worry level
            worry_level = (item * second_value if "*" in operation else item + second_value) % modulo
            # Next monkey id
            next_monkey_id = true_decisions[monkey_id] if worry_level % tests[monkey_id] == 0 else false_decisions[monkey_id]
            # Move to monkey
            monkeys_items[next_monkey_id].append(worry_level)

        total_items_per_monkey[monkey_id] = processed_count


if __name__ == "__main__":
    main()
