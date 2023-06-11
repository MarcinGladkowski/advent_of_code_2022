def is_on_edge(x: int, y: int, area: list) -> bool:
    if x == 0 or y == 0:
        return True

    if x == len(area[0]) - 1 or y == len(area[0]) - 1:
        return True


class Coordinates:

    __slots__ = ("x", "y", "on_edge")
    """
    on_edge: always visible
    """

    def __init__(self, x: int, y: int, on_edge: bool) -> None:
        self.x = x
        self.y = y
        self.on_edge = on_edge


class Tree:
    __slots__ = ("height", "coordinates")

    def __init__(self, height: int, coordinates: Coordinates):
        self.height = height
        self.coordinates = coordinates

    def __str__(self) -> str:
        return f"Tree X:{self.coordinates.x} Y:{self.coordinates.y} with height: {self.height}"


def transform_forrest(data: list):
    transformed_forrest = []
    for y, row in enumerate(data):
        for x, el in enumerate(row):
            transformed_forrest.append(
                Tree(el, Coordinates(x, y, is_on_edge(x, y, data)))
            )

    return transformed_forrest


def tree_visibility_on_axle_x(tree: Tree, area: list):
    x_trees = list(filter(lambda el: el.coordinates.y == tree.coordinates.y, area))

    left_side_trees_higher = list(filter(lambda el: el.height >= tree.height, x_trees[:][0:tree.coordinates.x]))
    right_side_trees_higher = list(filter(lambda el: el.height >= tree.height, x_trees[:][tree.coordinates.x + 1:]))

    return False if len(left_side_trees_higher) > 0 and len(right_side_trees_higher) > 0 else True


def tree_visibility_on_axle_y(tree: Tree, area: list):
    y_trees = list(filter(lambda el: el.coordinates.x == tree.coordinates.x, area))

    up_side_trees_higher = list(filter(lambda el: el.height >= tree.height, y_trees[:][0:tree.coordinates.y]))
    down_side_trees_higher = list(filter(lambda el: el.height >= tree.height, y_trees[:][tree.coordinates.y + 1:]))

    return False if len(up_side_trees_higher) > 0 and len(down_side_trees_higher) > 0 else True


def visible_trees(test_forrest: list):
    count = 0
    for tree in test_forrest:
        if tree.coordinates.on_edge:
            count += 1
            continue

        if tree_visibility_on_axle_x(tree, test_forrest) or tree_visibility_on_axle_y(tree, test_forrest):
            count += 1

    return count
