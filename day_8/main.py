from helper.main import read_data, sanitize, FILE

print("Day 8")

data = sanitize(read_data(FILE))

exercise_data = []
for row in data:
    exercise_data.append(list(map(lambda x: int(x), list(row))))

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
    __slots__ = ("height", "coordinates")

    def __init__(self, height: int, coordinates: Coordinates):
        self.height = height
        self.coordinates = coordinates


def transform_forrest(data: list):
    transformed_forrest = []
    for y, row in enumerate(data):
        for x, el in enumerate(row):
            transformed_forrest.append(
                Tree(el, Coordinates(x, y, is_on_edge(x, y, data)))
            )

    return transformed_forrest


transformed_forrest = transform_forrest(forrest)

assert 16 == len(list(filter(lambda tree: tree.coordinates.on_edge, transformed_forrest)))


def tree_visibility_on_axle_x(tree: Tree, area: list):
    x_trees = list(filter(lambda el: el.coordinates.y == tree.coordinates.y, area))

    left_side_trees_higher = list(filter(lambda el: el.height >= tree.height, x_trees[:][0:tree.coordinates.x]))
    right_side_trees_higher = list(filter(lambda el: el.height >= tree.height, x_trees[:][tree.coordinates.x + 1:]))

    return False if len(left_side_trees_higher) > 0 and len(right_side_trees_higher) > 0 else True


assert True == tree_visibility_on_axle_x(Tree(5, Coordinates(1, 1, False)), transformed_forrest)
assert False == tree_visibility_on_axle_x(Tree(3, Coordinates(2, 2, False)), transformed_forrest)


def tree_visibility_on_axle_y(tree: Tree, area: list):
    y_trees = list(filter(lambda el: el.coordinates.x == tree.coordinates.x, area))

    up_side_trees_higher = list(filter(lambda el: el.height >= tree.height, y_trees[:][0:tree.coordinates.y]))
    down_side_trees_higher = list(filter(lambda el: el.height >= tree.height, y_trees[:][tree.coordinates.y + 1:]))

    return False if len(up_side_trees_higher) > 0 and len(down_side_trees_higher) > 0 else True


assert tree_visibility_on_axle_y(Tree(5, Coordinates(1, 1, False)), transformed_forrest)
assert False == tree_visibility_on_axle_y(Tree(5, Coordinates(2, 2, False)), transformed_forrest)


def visible_trees(test_forrest: list):
    count = 0
    for tree in test_forrest:
        if tree.coordinates.on_edge:
            count += 1
            continue

        if tree_visibility_on_axle_x(tree, test_forrest) or tree_visibility_on_axle_y(tree, test_forrest):
            count += 1

    return count


assert 21 == visible_trees(transformed_forrest)
assert 1715 == visible_trees(transform_forrest(exercise_data))
