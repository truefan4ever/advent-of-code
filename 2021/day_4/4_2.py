def main():
    with open('4_1.txt', 'r') as f:
        numbers = [int(i) for i in f.read().split(',')]
    
    with open('4_2.txt', 'r') as f:
        raw_boards = f.read().split('\n\n')

    boards = transform_boards(raw_boards)
    
    print(play_bingo(numbers, boards))

    
def transform_boards(raw_boards):
    boards = []
    for i in raw_boards:
        boards.append(i.split('\n'))

    b_1 = []
    for board in boards:
        b_2 = []
        for row in board:
            r = list(filter(None, row.split(' ')))
            transformed_row = [{int(i): False} for i in r]
            b_2.append(transformed_row)
        
        b_1.append(b_2)
    
    return b_1


def play_bingo(nums, boards):
    for num in nums:
        mark_numbers(num, boards)
        index = check_state(boards)
        if index is True:
            res = num * sum_unmarked_nums(boards[0])
            return res


def sum_unmarked_nums(board):
    unmarked_sum = 0
    for row in board:
        for element in row:
            num = list(element.keys())[0]
            if not element[num]:
                unmarked_sum += num
    
    return unmarked_sum


def mark_numbers(num, boards):
    for board in boards:
        for row in board:
            for element in row:
                if num in element:
                    element[num] = True


def check_state(boards):
    for index, board in enumerate(boards):
        # check if all row is marked
        for row in board:
            states = []
            for element in row:
                states.append(*element.values())
            if all(states):
                boards.pop(index)
                print('popped2')
                print(len(boards))
                if len(boards) == 1:
                    return True
                else:
                    return None 
        
        # check if all column is marked
        for i, _ in enumerate(board[0]):
            states = []
            for row in board:
                states.append(*row[i].values())
            
            if all(states):
                boards.pop(index)
                print('popped1')
                print(len(boards))
                if len(boards) == 1:
                    return True
                else:
                    return None 


if __name__ == "__main__":
    main()
