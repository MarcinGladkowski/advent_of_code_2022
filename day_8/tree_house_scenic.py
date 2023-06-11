from day_8.forrest import transform_forrest, Tree, Coordinates

forrest = [
    [3, 0, 3, 7, 3],
    [2, 5, 5, 1, 2],
    [6, 5, 3, 3, 2],
    [3, 3, 5, 4, 9],
    [3, 5, 3, 9, 0]
]

test_forrest = transform_forrest(forrest)


def scenic_for_tree_axle_x(tree: Tree, area: list):

    x_trees = list(filter(lambda el: el.coordinates.y == tree.coordinates.y, area))

    left_trees = list(map(lambda row_tree: row_tree.height, x_trees[:tree.coordinates.x]))
    left_trees.sort(reverse=True)

    right_trees = list(map(lambda row_tree: row_tree.height, x_trees[tree.coordinates.x + 1:]))

    return count_visible_scenic_trees(left_trees, tree), count_visible_scenic_trees(right_trees, tree)


def scenic_for_tree_axle_y(tree: Tree, area: list):

    y_trees = list(filter(lambda el: el.coordinates.x == tree.coordinates.x, area))

    up_trees = list(map(lambda row_tree: row_tree.height, y_trees[:tree.coordinates.y]))
    up_trees.sort(reverse=True)

    down_trees = list(map(lambda row_tree: row_tree.height, y_trees[tree.coordinates.y + 1:]))

    return count_visible_scenic_trees(up_trees, tree), count_visible_scenic_trees(down_trees, tree)


def count_visible_scenic_trees(trees: list, tree: Tree):
    counter = 0
    for comparable_tree_height in trees:

        if tree.height > comparable_tree_height:
            counter += 1
            continue

        if tree.height == comparable_tree_height:
            counter += 1
            break

        break

    return counter



tree_to_calculate_scenic = Tree(5, Coordinates(2, 1, False))

scenic_for_tree_axle_y(tree_to_calculate_scenic, test_forrest)

assert scenic_for_tree_axle_x(tree_to_calculate_scenic, test_forrest) == (1, 2)
assert scenic_for_tree_axle_y(tree_to_calculate_scenic, test_forrest) == (1, 2)
