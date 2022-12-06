from collections import Counter
from helper.main import read_data, sanitize, FILE

print("Day 6")

data = sanitize(read_data(FILE))


def has_duplicate(counter: Counter):
    for k, v in counter.most_common():
        if v > 1:
            return True
    return False


def detect_marker(param):
    for i, partial in enumerate(param):
        if has_duplicate(Counter(param[i:i + 4])) is not True:
            return i + 4


assert has_duplicate(Counter('mjqj'))
assert 7 == detect_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
assert 11 == detect_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')
assert 10 == detect_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')
assert 6 == detect_marker('nppdvjthqldpwncqszvftbrmjlhg')
assert 5 == detect_marker('bvwbjplbgvbhsrlpgdmjqwftvncz')

print(detect_marker(data[0]))
