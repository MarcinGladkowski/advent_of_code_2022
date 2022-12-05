import re
from helper.main import read_data, sanitize, FILE, TEST_FILE

print("Day 5")

test_data = sanitize(read_data(TEST_FILE))


def parse_stack_elements(row: str):
    return re.findall('\[\w\]', row)


assert ['[D]'] == parse_stack_elements('    [D]')
assert ['[Z]', '[M]', '[P]'] == parse_stack_elements('[Z] [M] [P]')


def merge_pattern(row):
    pattern = '[X] [X] [X]'
    new = []
    for i, el in enumerate(pattern):
        if row[i] != ' ':
            new.append(row[i])
            continue
        new.append(el)

    return ''.join(new)


assert '[X] [D] [X]' == merge_pattern('    [D]    ')


def get_rows_count(row):
    return len(re.findall('\d', row))


assert 3 == get_rows_count(' 1   2   3 ')
