from helper.main import read_data, TEST_FILE, FILE

test_data = read_data(TEST_FILE)
data = read_data(FILE)

def sanitize(data: [str]):
    return [x.replace("\n", "") for x in data]

test_data = sanitize(test_data)

def find_share_item(rucksack: str):
    """
    Understand intersection using bitwise operator
    :param rucksack:
    :return:
    """
    split_index = int((len(rucksack)) / 2)

    left, right = rucksack[:split_index], rucksack[split_index:]

    intersection = list(set(left) & set(right))

    return intersection[0]


assert 'p' == find_share_item('vJrwpWtwJgWrhcsFMMfFFhFp')


def define_priority(symbol: str):
    """
    Lowercase item types a through z have priorities 1 through 26.
    Range 97 -> 122
    Base value 97-96=1 base: 96

    Uppercase item types A through Z have priorities 27 through 52. - ASCII dec code starts from 65
    We can set base value as 65-38=27
    Range 65 -> 90

    :return:
    """
    dec_ascii = ord(symbol)

    if 122 >= dec_ascii >= 97:
        return dec_ascii - 96

    if 90 >= dec_ascii >= 65:
        return dec_ascii - 38


def priority_sum(data: [str]):
    return sum(define_priority(find_share_item(item)) for item in data)


assert 27 == define_priority('A')
assert 1 == define_priority('a')
assert 157 == priority_sum(test_data)
# solution for part I
print(priority_sum(data))


def priority_of_three(data: [str]):
    """
    chunking to implement

    :param data:
    :return:
    """
    chunks = [
        data[:3],
        data[3:6]
    ]

    share_items = []
    for chunk in chunks:
        share_items.append(
            list(set(chunk[0]) & set(chunk[1]) & set(chunk[2]))
        )

    return sum([define_priority(x[0]) for x in share_items])


assert 70 == priority_of_three(test_data)