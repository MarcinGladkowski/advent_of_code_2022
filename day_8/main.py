from day_8.tree_house_scenic import highest_tree_scenic
from helper.main import read_data, sanitize, FILE
from forrest import Tree, Coordinates, transform_forrest, visible_trees, tree_visibility_on_axle_x, tree_visibility_on_axle_y

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

transformed_forrest = transform_forrest(forrest)

assert 16 == len(list(filter(lambda tree: tree.coordinates.on_edge, transformed_forrest)))


assert True == tree_visibility_on_axle_x(Tree(5, Coordinates(1, 1, False)), transformed_forrest)
assert False == tree_visibility_on_axle_x(Tree(3, Coordinates(2, 2, False)), transformed_forrest)


assert tree_visibility_on_axle_y(Tree(5, Coordinates(1, 1, False)), transformed_forrest)
assert False == tree_visibility_on_axle_y(Tree(5, Coordinates(2, 2, False)), transformed_forrest)


assert 21 == visible_trees(transformed_forrest)

# answers
assert 1715 == visible_trees(transform_forrest(exercise_data))
assert 374400 == highest_tree_scenic(transform_forrest(exercise_data))