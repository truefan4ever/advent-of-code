from enum import Enum

class Opponent(str, Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"

class Me(str, Enum):
    ROCK = "X"
    PAPER = "Y"
    SCISSORS = "Z"

class STATES(str, Enum):
    LOSE = "X"
    DRAW = "Y"
    WIN = "Z"

MY_ELEMENT_SCORES = {
    Me.ROCK: 1,
    Me.PAPER: 2,
    Me.SCISSORS: 3
}

SCORES = {
    ((Opponent.PAPER, Me.ROCK), (Opponent.ROCK, Me.SCISSORS), (Opponent.SCISSORS, Me.PAPER)): 0,
    ((Opponent.PAPER, Me.PAPER), (Opponent.ROCK, Me.ROCK), (Opponent.SCISSORS, Me.SCISSORS)): 3,
    ((Opponent.PAPER, Me.SCISSORS), (Opponent.ROCK, Me.PAPER), (Opponent.SCISSORS, Me.ROCK)): 6,
}
REVERSED_SCORES = {val: key for key, val in SCORES.items()}

STATES_SCORES_MAPPING = {
    STATES.WIN: 6,
    STATES.DRAW: 3,
    STATES.LOSE: 0,
}


def main():
    with open('2.txt', 'r') as f:
        data = [tuple(round_.split(' ')) for round_ in f.read().split('\n')]
        return count_total_score(data=preprocess_data(data))


def preprocess_data(data: list) -> list:
    processed_data = []
    for round_ in data:
        opponent_decision, state_ = round_
        score_to_get = STATES_SCORES_MAPPING[state_]
        score_combinations = REVERSED_SCORES[score_to_get]
        for combination in score_combinations:
            if combination[0] == opponent_decision:
                processed_data.append(combination)
                break

    return processed_data


def count_total_score(data: list) -> int:
    print(data)
    total_score = 0
    for round_ in data:
        for combinations, score in SCORES.items():
            if round_ in combinations:
                total_score += MY_ELEMENT_SCORES[round_[1]] + score
                break
        
    return total_score


if __name__ == "__main__":
    print(main())
