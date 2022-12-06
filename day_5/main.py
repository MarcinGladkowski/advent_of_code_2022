import re
from helper.main import read_data, sanitize, FILE, TEST_FILE

print("Day 5")

test_data = sanitize(read_data(TEST_FILE))


def parse_stack_elements(row: str):
    return re.findall('\[\w\]', row)


assert ['[D]'] == parse_stack_elements('    [D]')
assert ['[Z]', '[M]', '[P]'] == parse_stack_elements('[Z] [M] [P]')


def merge_pattern(pattern: str, row: str):
    new = []
    for i, el in enumerate(pattern):

        try:
            row[i]
        except:
            new.append(el)
            continue

        if row[i] != ' ':
            new.append(row[i])
            continue
        new.append(el)

    return ''.join(new)


assert '[X] [D] [X]' == merge_pattern('[X] [X] [X]', '    [D]    ')
assert '[X] [D] [X]' == merge_pattern('[X] [X] [X]', '    [D]')


def get_columns_count(row):
    return len(re.findall('\d', row))


assert 3 == get_columns_count(' 1   2   3 ')


def is_columns_numbers_row(row):
    return True if get_columns_count(row) else False


def create_pattern(columns_number: int):
    pattern = ''

    for i, _ in enumerate(range(columns_number)):
        pattern += '[X]'

        if i < columns_number - 1:
            pattern += ' '

    return pattern


assert '[X] [X] [X] [X]' == create_pattern(4)


def create_stacks(columns_count: int):
    return {x: [] for x in range(columns_count + 1) if x}


def fill_stacks(data: [str]):
    columns = 0
    columns_index = 0
    for i, row in enumerate(data):
        if is_columns_numbers_row(row):
            columns = get_columns_count(row)
            columns_index = i
            break

    pattern = create_pattern(columns)

    rows = []
    for i, row in enumerate(data):
        if i < columns_index:
            rows.append(
                parse_stack_elements(
                    merge_pattern(pattern, row)
                )
            )

    stacks = create_stacks(columns)

    for row in rows:
        for i, el in enumerate(row):
            if el != '[X]':
                stacks[i + 1].append(el)

    return stacks


assert {1: ['[N]', '[Z]'], 2: ['[D]', '[C]', '[M]'], 3: ['[P]']} == fill_stacks(test_data)


def sort_stacks(stacks: dict):
    for k, v in stacks.items():
        v.reverse()
        stacks[k] = v

    return stacks


assert {1: ['[Z]', '[N]'], 2: ['[M]', '[C]', '[D]'], 3: ['[P]']} == sort_stacks(
    {1: ['[N]', '[Z]'], 2: ['[D]', '[C]', '[M]'], 3: ['[P]']})


def parse_step(move: str):
    return list(map(lambda x: int(x), re.findall("\d", move)))


assert [1, 2, 1] == parse_step("move 1 from 2 to 1")


def move_elements(stacks: dict, step: [int]):
    elements_count = step[0]
    from_stack = step[1]
    to_stack = step[2]

    elements_to_move = stacks[from_stack][-elements_count:]

    for el in elements_to_move:
        stacks[from_stack].remove(el)

    stacks[to_stack] = stacks[to_stack] + elements_to_move

    return stacks



assert {1: ['[Z]', '[N]', '[D]'], 2: ['[M]', '[C]'], 3: ['[P]']} == move_elements(
    {1: ['[Z]', '[N]'], 2: ['[M]', '[C]', '[D]'], 3: ['[P]']}, [1, 2, 1])
