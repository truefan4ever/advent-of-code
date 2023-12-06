from enum import Enum


class Opponent(str, Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"


class Me(str, Enum):
    ROCK = "X"
    PAPER = "Y"
    SCISSORS = "Z"


MY_ELEMENT_SCORES = {Me.ROCK: 1, Me.PAPER: 2, Me.SCISSORS: 3}

SCORES = {
    (
        (Opponent.PAPER, Me.ROCK),
        (Opponent.ROCK, Me.SCISSORS),
        (Opponent.SCISSORS, Me.PAPER),
    ): 0,
    (
        (Opponent.PAPER, Me.PAPER),
        (Opponent.ROCK, Me.ROCK),
        (Opponent.SCISSORS, Me.SCISSORS),
    ): 3,
    (
        (Opponent.PAPER, Me.SCISSORS),
        (Opponent.ROCK, Me.PAPER),
        (Opponent.SCISSORS, Me.ROCK),
    ): 6,
}


def main():
    with open("2.txt", "r") as f:
        data = [tuple(round_.split(" ")) for round_ in f.read().split("\n")]
        return count_total_score(data=data)


def count_total_score(data: list) -> int:
    total_score = 0
    for round_ in data:
        for combinations, score in SCORES.items():
            if round_ in combinations:
                total_score += MY_ELEMENT_SCORES[round_[1]] + score
                break

    return total_score


if __name__ == "__main__":
    print(main())
