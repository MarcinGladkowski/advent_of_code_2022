from typing import Type

forrest = [
    [3, 0, 3, 7, 3],
    [2, 5, 5, 1, 2],
    [6, 5, 3, 3, 2],
    [3, 3, 5, 4, 9],
    [3, 5, 3, 9, 0]
]


def is_on_edge(x: int, y: int, area: list) -> bool:
    if x == 0 or y == 0:
        return True

    if x == len(area[0]) - 1 or y == len(area[0]) - 1:
        return True


class Coordinates:
    """
    on_edge: always visible
    """

    def __init__(self, x: int, y: int, on_edge: bool) -> None:
        self.x = x
        self.y = y
        self.on_edge = on_edge


class Tree:
    def __init__(self, height: int, coordinates: Coordinates):
        self.height = height
        self.coordinates = coordinates


transformed_forrest = []

for y, row in enumerate(forrest):
    for x, el in enumerate(row):
        transformed_forrest.append(
            Tree(el, Coordinates(x, y, is_on_edge(x, y, forrest)))
        )

assert 16 == len(list(filter(lambda tree: tree.coordinates.on_edge, transformed_forrest)))


def trees_on_axle_x(tree: Tree, area: list):
    x_trees = list(filter(lambda el: el.coordinates.y == tree.coordinates.y, area))

    left_side_trees_higher = filter(lambda el: el.height < tree.height, x_trees[:][0:tree.coordinates.x])
    right_side_trees_higher = filter(lambda el: el.height < tree.height, x_trees[:][tree.coordinates.x + 1:])

    return True if len(list(left_side_trees_higher)) > 0 and len(list(right_side_trees_higher)) > 0 else False


assert True == trees_on_axle_x(Tree(5, Coordinates(1, 1, False)), transformed_forrest)
assert False == trees_on_axle_x(Tree(5, Coordinates(2, 2, False)), transformed_forrest)


def visible_trees(forrest: list):
    count = 0
    for tree in forrest:
        if tree.coordinates.on_edge:
            count = count + 1

    return count


print(
    visible_trees(transformed_forrest)
)
