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