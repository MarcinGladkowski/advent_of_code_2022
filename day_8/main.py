from typing import Type

forrest = [
    [3, 0, 3, 7, 3],
    [2, 5, 5, 1, 2],
    [6, 5, 3, 3, 2],
    [3, 3, 5, 4, 9],
    [3, 5, 3, 9, 0]
]


class Coordinates:

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


grid = {
    'top_left': Coordinates(1, 1),
    'top_right': Coordinates(len(forrest) - 1, 1),
    'bottom_left': Coordinates(1, len(forrest) - 1),
    'bottom_right': Coordinates(len(forrest) - 1, len(forrest) - 1),
}


class Axle:

    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def on_axle(self, coord):
        return True if self.a < coord < self.b else False


xaxle = Axle(0, 4)
yaxle = Axle(0, 4)
"""
first step: display elements inside grid
"""
coords_to_check = []
for i, row in enumerate(forrest):
    for j, el in enumerate(row):
        coords = Coordinates(j, i)
        if xaxle.on_axle(coords.x) and yaxle.on_axle(coords.y):
            coords_to_check.append(coords)
            continue

assert 9 == len(coords_to_check)


def filter_higher_trees(tree_index: int, row: list):
    return len(list(filter(lambda x: x >= row[tree_index], row))) > 0


assert filter_higher_trees(2, [2, 5, 5, 1, 2])


def get_column_values(column_index: int, forrest: list):
    return [x[column_index] for x in forrest]


def check_visibility(coords_to_review: list, forrest: list):
    visible_coords = []
    for coord in coords_to_review:

        if filter_higher_trees(coord.x, forrest[coord.y]) \
                or filter_higher_trees(coord.y, get_column_values(coord.x, forrest)):
            visible_coords.append(coord)

    return visible_coords


result = check_visibility(coords_to_check, forrest)

print(len(result))
