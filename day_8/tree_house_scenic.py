import functools
import math
from typing import Callable

from day_8.forrest import transform_forrest, Tree, Coordinates

forrest = [
    [3, 0, 3, 7, 3],
    [2, 5, 5, 1, 2],
    [6, 5, 3, 3, 2],
    [3, 3, 5, 4, 9],
    [3, 5, 3, 9, 0]
]

test_forrest = transform_forrest(forrest)


def scenic_for_tree_axle_x(tree: Tree, area: list, count_scenic: Callable):
    x_trees = list(filter(lambda el: el.coordinates.y == tree.coordinates.y, area))

    left_trees = list(map(lambda row_tree: row_tree.height, x_trees[:tree.coordinates.x]))
    left_trees.sort(reverse=True)

    right_trees = list(map(lambda row_tree: row_tree.height, x_trees[tree.coordinates.x + 1:]))

    return count_scenic(left_trees, tree), count_scenic(right_trees, tree)


def scenic_for_tree_axle_y(tree: Tree, area: list, count_scenic: Callable):
    y_trees = list(filter(lambda el: el.coordinates.x == tree.coordinates.x, area))

    up_trees = list(map(lambda row_tree: row_tree.height, y_trees[:tree.coordinates.y]))
    up_trees.sort(reverse=True)

    down_trees = list(map(lambda row_tree: row_tree.height, y_trees[tree.coordinates.y + 1:]))

    return count_scenic(up_trees, tree), count_scenic(down_trees, tree)


def count_visible_scenic_trees(trees: list, tree: Tree):
    counter = 0

    if len(trees) == 0:
        return 1

    for comparable_tree_height in trees:

        if tree.height > comparable_tree_height:
            counter += 1
            continue

        counter += 1
        break

    return counter


tree_to_calculate_scenic = Tree(5, Coordinates(2, 1, False))

assert scenic_for_tree_axle_x(tree_to_calculate_scenic, test_forrest, count_visible_scenic_trees) == (1, 2)
assert scenic_for_tree_axle_y(tree_to_calculate_scenic, test_forrest, count_visible_scenic_trees) == (1, 2)


def highest_tree_scenic(scenic_forrest: list):
    highest_scenic = 0
    for tree in scenic_forrest:
        scenic_count_for_tree = scenic_for_tree_axle_x(tree, scenic_forrest, count_visible_scenic_trees) \
                                + scenic_for_tree_axle_y(tree, scenic_forrest, count_visible_scenic_trees)

        calculated = functools.reduce(lambda a, b: a * b, scenic_count_for_tree)

        if calculated > highest_scenic:
            highest_scenic = calculated

    return highest_scenic


assert 16 == highest_tree_scenic(test_forrest)
