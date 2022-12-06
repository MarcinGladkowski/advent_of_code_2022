from collections import Counter
from helper.main import read_data, sanitize, FILE

print("Day 6")

data = sanitize(read_data(FILE))


def has_duplicate(counter: Counter):
    for k, v in counter.most_common():
        if v > 1:
            return True
    return False


def detect_marker(param, distinct_characters=4):
    for i, partial in enumerate(param):
        if has_duplicate(Counter(param[i:i + distinct_characters])) is not True:
            return i + distinct_characters


assert has_duplicate(Counter('mjqj'))
assert 7 == detect_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
assert 11 == detect_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')
assert 10 == detect_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')
assert 6 == detect_marker('nppdvjthqldpwncqszvftbrmjlhg')
assert 5 == detect_marker('bvwbjplbgvbhsrlpgdmjqwftvncz')

print(detect_marker(data[0]))


assert 19 == detect_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14)
assert 23 == detect_marker('bvwbjplbgvbhsrlpgdmjqwftvncz', 14)
assert 23 == detect_marker('nppdvjthqldpwncqszvftbrmjlhg', 14)
assert 29 == detect_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14)
assert 26 == detect_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14)


print(detect_marker(data[0], 14))
