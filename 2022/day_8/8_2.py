def main():
    with open('8.txt', 'r') as f:
        data = [[int(i) for i in line] for line in f.read().split('\n')]
        return calculate_max_scenic_score(data)


def get_side_score(tree: int, trees: list) -> int:
    if tree not in trees and max(trees) < tree:
        return len(trees)

    temp_trees = []
    for tree_ in trees:
        temp_trees.append(tree_)
        if tree_ >= tree:
            break

    return len(temp_trees)


def calculate_max_scenic_score(matrix: list) -> int:
    scenic_scores = []

    for row_index, row in enumerate(matrix):
        for tree_index, tree in enumerate(row):
            if row_index == 0 or row_index == len(matrix) - 1 or tree_index == 0 or tree_index == len(row) - 1:
                # don't check borders
                continue

            # Check from the left
            trees_to_the_left = row[:tree_index]
            trees_to_the_left.reverse()
            left_score = get_side_score(tree=tree, trees=trees_to_the_left)

            # Check from the right
            trees_to_the_right = row[tree_index + 1:]
            right_score = get_side_score(tree=tree, trees=trees_to_the_right)

            # Check from the top
            trees_to_the_top = [row[tree_index] for index, row in enumerate(matrix) if index < row_index]
            trees_to_the_top.reverse()
            top_score = get_side_score(tree=tree, trees=trees_to_the_top)

            # Check from the bottom
            trees_to_the_bottom = [row[tree_index] for index, row in enumerate(matrix) if index > row_index]
            bottom_score = get_side_score(tree=tree, trees=trees_to_the_bottom)

            scenic_scores.append(left_score * right_score * top_score * bottom_score)

    return max(scenic_scores)


if __name__ == "__main__":
    print(main())
