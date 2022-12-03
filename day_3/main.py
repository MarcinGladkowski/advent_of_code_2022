from helper.main import read_data, TEST_FILE

data = read_data(TEST_FILE)

sanitize_data = [x.replace("\n", "") for x in data]


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


    Uppercase item types A through Z have priorities 27 through 52. - ASCI dec code starts from 65
    We can set base value as 65-38=27

    :return:
    """
    return ord(symbol) - 38


assert 27 == define_priority('A')