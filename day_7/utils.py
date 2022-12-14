from day_7.main import Dir


def print_tree(el, nested: str = ""):
    nested += "\t"
    if isinstance(el, Dir):
        for i in el.children:
            print(nested, str(i), i.name, i.size)
            print_tree(i, nested)


def filter_size(data: list):
    return map(lambda x: x.size, data)

def filter_by_size(data: list, size: int = 100_000):
    return filter(lambda x: x < size, map(lambda x: x.size, data))


def filter_directories(el: Dir, dirs: list):
    """
    Flat directories instead cumulating sum walking by directories tree
    """
    if isinstance(el, Dir):
        dirs.append(el)
        for i in el.children:
            filter_directories(i, dirs)
