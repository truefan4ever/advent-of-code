def main():
    with open('8.txt', 'r') as f:
        data = [[int(i) for i in line] for line in f.read().split('\n')]
        return find_visible_trees(data)


def find_visible_trees(matrix: list) -> int:
    visible_trees = 0
    # Add border trees
    visible_trees += len(matrix[0]) * 2 + (len(matrix) - 2) * 2

    for row_index, row in enumerate(matrix):
        for tree_index, tree in enumerate(row):
            if row_index == 0 or row_index == len(matrix) - 1 or tree_index == 0 or tree_index == len(row) - 1:
                # don't check borders
                continue

            # Check from the left
            trees_to_the_left = row[:tree_index]
            if tree not in trees_to_the_left and max(trees_to_the_left) < tree:
                visible_trees += 1
                continue

            # Check from the right
            trees_to_the_right = row[tree_index + 1:]
            if tree not in trees_to_the_right and max(trees_to_the_right) < tree:
                visible_trees += 1
                continue

            # Check from the top
            trees_to_the_top = [row[tree_index] for index, row in enumerate(matrix) if index < row_index]
            if tree not in trees_to_the_top and max(trees_to_the_top) < tree:
                visible_trees += 1
                continue

            # Check from the bottom
            trees_to_the_bottom = [row[tree_index] for index, row in enumerate(matrix) if index > row_index]
            if tree not in trees_to_the_bottom and max(trees_to_the_bottom) < tree:
                visible_trees += 1
                continue

    return visible_trees


if __name__ == "__main__":
    print(main())
